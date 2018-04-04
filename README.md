## Networking Survival Kit

## About:
*note: Only works with Python V2.x.x*
<br>
Basic Python network reconnaissance scripts that uses urlib2, BeautifulSoup, socket, and several inbuilt python libraries. <br>
    
## Current Functions 

**System Info Tool** <br>
Returns string of host machine. To run this function, call to sysInfo.py. <br>
cmd output: thisComputerName <br>

**IP Mapping** <br>
Returns IP Address string.This converts domain name to the ip address assigned. To run this function, call to IPmap.py<br>
cmd output:enter domain name : google.com <br>
returns *172.217.11.174* <br>
crtl+c to exit script.

**Port Scanner** <br>
Scans for open ports on targeted domain. Call to PortScan.py to run script<br>
example output: <br>
enter : google.com <br>
172.217.11.174 <br>
starting port : 1 <br>
ending port : 1024 <br>
PORT 1 OPEN <br>
PORT 3 OPEN <br>
...<br>

 
**Client Browser** <br>
Enter domain name of website and returns an html file string.

**Mac Address Lookup** <br>
Returns System infomation on targeted MAC Addresses. Uses macvendors API.<br>

**WebSpider Bitcoin***<br>
Script that returns bitcoin cryptocurrency value (Single, Market Cap, and 24 Volume) to USD currency with time stamps that writes it into bitcoin.txt. <br>
Open bitcoin.txt and run webSpider.py to grab single, market cap, and 24 volume currency rate. <br>
****features in webspider.py**** <br>
Scrap('https://coinmarketcap.com/currencies/bitcoin/').getSingle() returns USD currency of a single bitcoin<br>
Scrap('https://coinmarketcap.com/currencies/bitcoin/').getMarketValue() returns the Market Cap of bitcoin to USD currency<br>
Scrap('https://coinmarketcap.com/currencies/bitcoin/').getVolume24hr() returns 24hour volume of bitcoin to USD currency<br>
