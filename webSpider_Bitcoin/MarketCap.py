def getMarketValue(soup):
    MarkCapDiv = soup.find("div", {"class": "coin-summary-item-detail details-text-medium"})
    MarkCapValues = MarkCapDiv.find_all("span")
    USDvalue = MarkCapValues[1].text + " " + MarkCapValues[2].text
    BTCvalue = re.findall(r'\d+(?:,\d+)?',  MarkCapValues[3].text.strip())
    string = """
    Market Cap
    ---------------
    ${USD} => BTC{BTC}
    ---------------
    """
    #returns Market Value value in USD
    return string.format(USD = USDvalue, BTC = BTCvalue)