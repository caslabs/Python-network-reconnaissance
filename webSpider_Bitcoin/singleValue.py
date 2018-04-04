def getSingle(soup):
  testTag = soup.find_all("span", {"id": "quote_price"})
  OverallVal = "1 BTC => "

  for tag in testTag:
    specificVal = tag.find_all("span")
    for tag in specificVal:
      OverallVal+= " " + tag.text

    #returns 1BTC value in USD
  string = """
  Single Value
  ---------------
  {value}
  ---------------

  """
  # return string.format(value = OverallVal)
  return string.format(value = OverallVal)