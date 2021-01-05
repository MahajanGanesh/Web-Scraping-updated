# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup

# website = 'http://www.get2drive.com/car-dealerships'
# uClient = uReq(website)
# page_html = uClient.read()
# uClient.close()
# page_of_deler = soup(page_html, "html.parser")
# div = page_of_deler.find_all("ul", {'class':'ulList cols2'})
# for d in div:
#     print(div)
# # d = div.find_all("li")
# # for d in div:
# #     print(d)
import requests

r = requests.get('https://httpbin.org/ip')
print(r.status_code)
# import random
# from bs4 import BeautifulSoup as bs
#
# proxies = [
#     '173.208.103.45:8800'
#     '173.208.103.235:8800'
#     '92.114.60.120:8800'
#     '192.126.219.181:8800'
#     '50.31.107.101:8800'
#     '50.31.105.233:8800'
#     '173.208.39.131:8800'
#     '216.158.192.210:8800'
#     '50.31.106.176:8800'
#     '104.129.50.88:8800'
#     '173.208.103.153:8800'
#     '173.208.36.60:8800'
#     '173.234.165.66:8800'
#     '50.31.106.109:8800'
#     '67.202.113.35:8800'
# ]
# def get_session(proxies):
#     # construct an HTTP session
#     session = requests.Session()
#     # choose one random proxy
#     proxy = random.choice(proxies)
#     session.proxies = {"http": proxy, "https": proxy}
#     return session
#
# for i in range(5):
#     s = get_session(proxies)
#     try:
#         print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
#     except Exception as e:
#         print(e)