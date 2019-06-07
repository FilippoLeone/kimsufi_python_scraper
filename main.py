# coding: utf8
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import json
import smtplib
import requests
import credentials

def send_telegram_message(message):
        requests.get(
                f'https://api.telegram.org/bot{credentials.telegram_token}/sendMessage?chat_id={credentials.telegram_channel}&text={message}&parse_mode=markdown'
        )

def sendmail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # compose and send the email

def prior_check():
        try:
                with open('serverlog.json', 'r', encoding='utf8') as serverlog:
                        jsondata = json.load(serverlog)
                return jsondata
        except FileExistsError:
                return False

if __name__ == '__main__':
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path=credentials.firefox_path, options=options)
        # Path to your geckodriver, you can download it from here https://github.com/mozilla/geckodriver/releases
        driver.get('http://www.kimsufi.com/en/servers.xml')
        time.sleep(5)
        status = driver.execute_script('function a() {return document.readyState;};return a();')
        if status == 'complete':
                html_doc = driver.page_source
                driver.quit()
                soup = BeautifulSoup(html_doc, 'html.parser')
                tables = soup.findAll('table', {'class' : 'full homepage-table'})
                serverdict = {}

                for index,table in enumerate(tables):
                        if index == 0:
                                english_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})
                        else:
                                canadian_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})

                for server in english_servers:
                        #serverinfo = server 
                        serverinfo = 'English: '+''.join(server.text.replace('\n','').replace(' ','').replace('ex.VATCurrentlybeingreplenishedHaveyouthoughtaboutchoosingaSoyouStartserver?Victimofitssuccess!Availablesoon.',''))
                        cart_elements = server.findAll('td', {'class' : 'btn-order-ks2014'})
                        for cart_element in cart_elements:
                                try:
                                        cart_element['style'];serverdict[serverinfo] = 'Not Available'
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
        #print(f"{serverdict}")
        oldjson = prior_check()
        if oldjson:
                for (key_old,value_old), (key_new,value_new) in zip(oldjson.items(), serverdict.items()):
                        if value_old != value_new:
                                send_telegram_message(f"*ALERT!*\nThe server:\n*{key_new}*\nChanged availability and is now: \n*{value_new}*.")
                                #print(f"{key_new} changed availability and is now: {value_new}.")

        with open('serverlog.json', 'w', encoding='utf8') as jsonlog:
                jsonlog.write(json.dumps(serverdict, ensure_ascii=False, indent=4))