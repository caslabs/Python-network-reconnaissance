  def getVolume24hr(soup):
    VolumeDiv = soup.find_all("div", {"class": "coin-summary-item"})[1]
    btcPrice = re.findall(r'\d+(?:,\d+)?', VolumeDiv.find_all("span")[4].text)
    string = """
    {title} 
    ---------------
    {USD} => {BTC}BTC
    ---------------

    """
    #returns getVolume24hr value in USD
    return string.format(title = VolumeDiv.find("h3").text, USD= "$" + VolumeDiv.find_all("span")[1].text, BTC=btcPrice)
