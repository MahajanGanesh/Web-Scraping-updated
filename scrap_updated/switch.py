from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class Auto():
    filename = "buy-auto.csv"
    global f
    f = open(filename, "w")
    headers = "Dealer_name, Dealer_contact , Dealer_address, Dealer_website\n"
    f.write(headers)

    def __init__(self):
        for i in range(1, 6):
            website = 'http://www.buy-auto.co.uk/dealers/search/page/'
            website = website + str(i)
            self.Scrap(website)

    def Scrap(self, website):
        uClient = uReq(website)
        page_html = uClient.read()
        uClient.close()
        page_of_deler = soup(page_html, "html.parser")
        con = page_of_deler.findAll('div', {'car_dialer'})
        for container in con:
            name = container.find('a', class_='title open-car-link').text
            # print("Name :", name)

            mobile = container.find('div', class_='tel').text
            # print("Mobile :", mobile)

            address = container.find('div', class_='adress').text.strip()
            # print("Address :", address)

            link = container.find('a', class_='link-off_gray') if container.find('a', class_='link-off_gray') else 'No Website Found'
            if link == "No Website Found":
                # print("Link :", link)
                link = " "
            else:
                # print("Link :", link['href'])
                link = link['href']
            f.write(name.replace(",", "") + "," + mobile.replace(",", "") + "," + address.replace(",","") + "," + link + "\n")

class Drive():
    global link, str, str1, link1
    filename = "get2drive.csv"
    f = open(filename, "w")
    headers = "Dealer_name, Dealer_contact , Dealer_address, Dealer_website\n"
    f.write(headers)
    link = []
    link1 = []
    def __init__(self):
        # website = input("Enter WebLink : ")
        website = 'http://www.get2drive.com/car-dealerships'
        self.Script(website)

    def Script(self,website):
        self.n = website
        self.uClient = uReq(website)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_of_deler = soup(self.page_html, "html.parser")
        self.Scrap()

    def Scrap(self):
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
            self.Loops()
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

    def Loops(self):
        global link
        link1 = link
        link = []
        n = len(link1)
        for i in range(n):
            s = link1[i]
            self.Script(s)

n = int(input("Enter 1 to scrap buy-auto.co.uk OR Enter 2 to scrap get2drive.com : \t"))
if n == 1:
    Auto()
else:
    Drive()