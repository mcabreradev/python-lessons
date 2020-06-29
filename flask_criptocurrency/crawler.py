from bs4 import BeautifulSoup
from time import sleep
from urllib.request import urlopen, Request

class Crawler():
    url = 'https://coinranking.com'
    data = []

    def __init__(self):
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        self.html = urlopen(self.req).read()
        self.bs = BeautifulSoup(self.html, 'html.parser')

        print('Init Crawler')
        self.parseData()

    def getHtml(self):
        print('Crawling data..')
        return self.bs.find('tbody', class_="table__body").find_all('tr', class_="table__row")[0:5]

    def parseData(self):
        rows = self.getHtml()
        for i, row in enumerate(rows):
          img = row.find('span', class_="profile__logo-background").find('img')['src']
          cryptocurrency = row.find('span', class_="profile__name").get_text().strip().replace('\n', '')
          values = row.find_all('div', class_="valuta")
          price = values[0].get_text().strip().replace('\n', '').replace(' ', '').replace('$', '')
          market_cap = values[1].get_text().strip().replace('\n', '')
          change = row.find('div', class_="change").find('span').get_text().strip().replace('\n', '')
          sign = row.find('div', class_="change").find('img')['alt'].lower()
          self.setData({'order': i+1,'cryptocurrency': cryptocurrency, 'price': price,'market_cap': market_cap, 'change': change, 'img': img , 'sign': sign})
          sleep(1)

    def setData(self, cripto):
        self.data.append(cripto)
        print('Geting {} details..'.format(cripto.cryptocurrency))

    def getData(self):
        self.parseData()
        return self.data


craw = Crawler()
print(craw)
