# coding: utf8
from scraper import Scraper
from logger import Logger
from communicator import Communicator
import credentials
from bs4 import BeautifulSoup

if __name__ == '__main__':
        # Importing my wrappers
        Scraper = Scraper()
        Logger = Logger(__file__)
        Communicator = Communicator()

        Scraper.create_driver()
        html_doc = Scraper.fetch_page('http://www.kimsufi.com/en/servers.xml')
        # Kimsufi target page
        status = Scraper.run_javascript('function a() {return document.readyState;};return a();')
        # Is document.readyState set to complete? If not it's pointless to execute the target page needs to execute some JS before displaying the availability
        if status == 'complete':
                soup = BeautifulSoup(html_doc, 'html.parser')
                tables = soup.findAll('table', {'class' : 'full homepage-table'})
                # The two tables (English, Canadian) containing the server information 
                serverdict = {}
                
                for index,table in enumerate(tables):
                        if index == 0:
                                english_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})
                        else:
                                canadian_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})
                
                for server in english_servers:
                        serverinfo = 'English: '+''.join(server.text.replace('\n','').replace(' ','').replace('ex.VATCurrentlybeingreplenishedHaveyouthoughtaboutchoosingaSoyouStartserver?Victimofitssuccess!Availablesoon.',''))
                                # Dirty replace, might optimize with a proper split so we can also set personal alerts for a specific server/price/specs 
                        cart_elements = server.findAll('td', {'class' : 'btn-order-ks2014'})
                        for cart_element in cart_elements:
                                try:
                                        cart_element['style'];serverdict[serverinfo] = 'Not Available'
                                        # If the inline style of this element is set to display:none therefore exists set it to Not available
                                except KeyError:
                                        serverdict[serverinfo] = 'Available'

                for server in canadian_servers:
                        serverinfo = 'Canadian: '+''.join(server.text.replace('\n','').replace(' ','').replace('ex.VATCurrentlybeingreplenishedHaveyouthoughtaboutchoosingaSoyouStartserver?Victimofitssuccess!Availablesoon.',''))
                        cart_elements = server.findAll('td', {'class' : 'btn-order-ks2014'})
                        for cart_element in cart_elements:
                                try:
                                        cart_element['style'];serverdict[serverinfo] = 'Not Available';
                                except KeyError:
                                        serverdict[serverinfo] = 'Available';
        oldjson = Logger.get_json()
        if oldjson:
                for (key_old,value_old), (key_new,value_new) in zip(oldjson.items(), serverdict.items()):
                        if value_old != value_new:
                                Communicator.telegram_message(f"*ALERT!*\nThe server:\n*{key_new}*\nChanged availability and is now: \n*{value_new}*.", credentials.telegram_channel)
                                        # To make this a bit prettier...
        Logger.log_json(serverdict)
        Scraper.kill_driver()