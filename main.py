from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

if __name__ == '__main__':
        firefoxpath = r'C:\Users\Home\Desktop\kimsufi-scraper\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe'
        # Path to your geckodriver, you can download it from here https://github.com/mozilla/geckodriver/releases
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path=firefoxpath, options=options)
        driver.get('http://www.kimsufi.com/en/servers.xml')
        html_doc = driver.page_source
        driver.quit()
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        tables = soup.findAll('table', {'class' : 'full homepage-table'})

        for index,table in enumerate(tables):
                if index == 0:
                        english_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})
                else:
                        canadian_servers = table.findAll('tr', {'class' : 'zone-dedicated-availability'})

        for server in english_servers:
                cart_elements = server.findAll('td', {'class' : 'btn-order-ks2014'})
                for cart_element in cart_elements:
                        try:
                                cart_element['style'];print('English: Server not available')
                        except KeyError:
                                print('English: Server available')

        for server in canadian_servers:
                cart_elements = server.findAll('td', {'class' : 'btn-order-ks2014'})
                for cart_element in cart_elements:
                        try:
                                cart_element['style'];print('Canadian: Server not available')
                        except KeyError:
                                print('Canadian: Server available')