import re , urllib
import urllib2
import urllib.request
sites = "redbus".split()
u = urllib.request.urlopen("https://www.redbus.in/info/contactus")
text = u.read()
    #number = re.findall('[+0-9]{3}[0-9][10]',str(text))

