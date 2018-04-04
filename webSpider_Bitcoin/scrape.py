import urllib2
from bs4 import BeautifulSoup
import re
import datetime
import time

#scraping imports
from singleValue import getSingle
from MarketCap import getMarketValue
from VolumeRate import getVolume24hr

#automated
class Scrap:

  def __init__(self, url):
    self.url = url
    self.request = urllib2.Request(self.url);
    self.response = urllib2.urlopen( self.request )
    self.html = self.response.read();
    self.soup = BeautifulSoup(self.html, "html.parser")
    print (getSingle(self.soup))

  def getAll(self):
    #this calls every class functions
    sin =getSingle(self.soup)
    mv = getMarketValue(self.soup)
    v24 = getVolume24hr(self.soup)
    time = datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S")
    btcTXTFILE = open("bitcoin.txt", "w")
    btcTXTFILE.write(time + sin + mv + v24)
    btcTXTFILE.close()
    
while True:
    Scrap('https://coinmarketcap.com/currencies/bitcoin/').getAll()
    print("refreshed | " + datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S") )
    time.sleep(2) # wait one minute