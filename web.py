import urllib
try:
    while True:
        url = raw_input("website ->")
        request = urllib.urlopen("https://" + url)
        print("url")
        print "-"*30
        print(url)

        print("status code")
        print "-"*30
        print(request.getcode())

        print ("data")
        print "-"*30
        print (request.read())

        print ("request info")
        print "-"*30
        print (request.info())
except KeyboardInterrupt:
    pass
