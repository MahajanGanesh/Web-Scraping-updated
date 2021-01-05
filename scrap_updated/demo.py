import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class auto():
    filename = "buy-auto.csv"
    global f
    f = open(filename, "w")
    headers = "Dealer_name, Dealer_contact , Dealer_address, Dealer_website\n"
    f.write(headers)

    def __init__(self):
        for i in range(1, 6):
            website = 'http://www.buy-auto.co.uk/dealers/search/page/'
            website = website + str(i)
            self.scrap(website)

    def scrap(self, website):
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












































# import requests
# proxies = {
#     "https" : "67.202.113.35:8800",
#     "http" : "67.202.113.35:8800"
# }
# website = "https://youtube.com"
# r = requests.get(website, proxies=proxies)
# r.json()
# import requests
# requests.get("http://httpbin.org/get", proxies={"http": "185.206.129.54:8800"})
#
# from bs4 import BeautifulSoup
#
# res = requests.get('http://free-proxy-list.net')
# print(res.text)

# import bs4
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup

#
# website = 'http://www.get2drive.com/car-dealerships'
# uClient = uReq(website)
# page_html = uClient.read()
# uClient.close()
# page_of_deler = soup(page_html, "html.parser")
# con = page_of_deler.find('ul', {'ulList cols2'})
# for d in con:
#     str = 'http://www.get2drive.com'
#     str1 = str + d.a['href']
#     print(str1)
    # print("d = ", d.a['href'])
    # for b in d:
    #     # print("b = ", b.)
    #
    #     for c in b:
    #         print(c)
# for d in con:
#     print(d.find_all('li').a['href'])
# print(con.find_all('li')[0].a['href'])
# con = page_of_deler.findAll('ul', {'ulList cols2'})
# for d in con:
#     print(d.findAll('li').a)




