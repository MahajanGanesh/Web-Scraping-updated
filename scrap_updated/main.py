import bs4
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



class Web_scrap():
    filename = "get2drive.csv"
    f = open(filename, "w")
    headers = "Dealer_name, Dealer_contact , Dealer_address, Dealer_website\n"
    f.write(headers)
    global link, str, str1, link1
    link = []
    link1 = []
    def __init__(self):
        # website = input("Enter WebLink : ")
        website = 'http://www.get2drive.com/car-dealerships'
        self.script(website)

    def script(self,website):
        self.n = website
        self.uClient = uReq(website)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_of_deler = soup(self.page_html, "html.parser")
        self.scrap()

    def scrap(self):
        if self.page_of_deler.find('ul', {'ulList cols2'}):
            con = self.page_of_deler.find('ul', {'ulList cols2'})
            len1 = len(con)
            print(len1)
            for d in con:
                # print(type(d))
                str = 'http://www.get2drive.com'
                str1 = str + d.a['href']
                # print(str1)
                link.append(str1)
            self.loops()
        else :
            con = self.page_of_deler.findAll('div', {'vcard'})
            for container in con:
                name = container.find('p', class_='fn').strong.text
                # print(name)

                address = container.find('p', class_='adr').text
                # print(address)

                mobile1 = container.find('p', class_='tel').text
                mob = mobile1[7:20]
                # print(mob)

                if container.find('p', class_='url'):
                    dealer_link = container.find('p', class_='url').a['href']
                    # print(dealer_link)
                else:
                   dealer_link = " "
                   # print(dealer_link)
                f.write(name.replace(",", "") + "," + mob.replace(",", "") + "," + address.replace(",","") + "," + dealer_link + "\n")

    def loops(self):
        global link
        link1 = link
        link = []
        n = len(link1)
        for i in range(n):
            s = link1[i]
            self.script(s)

# r = Web_scrap()
# r.scrap()
# Web_scrap()