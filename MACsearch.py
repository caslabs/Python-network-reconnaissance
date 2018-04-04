import urllib2
import json
import codecs

MACaddr = raw_input("enter MAC address > ")
url = "http://macvendors.co/api/"

request = urllib2.Request(url+MACaddr, headers={'User-Agent' : "API Browser"}) 


response = urllib2.urlopen( request )
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

company =obj['result']['company']
address =obj['result']['address']

print(company.encode("ascii","replace"),address.encode("ascii","replace"))
