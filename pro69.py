import re,urllib
import urllib.request

sites = 'google yahoo'.split()
print(sites)
for web in sites:
    print('searching.....',web)
    u = urllib.request.urlopen("http://"+web+".com")
    text = u.read()
    title = re.findall('<title>.*</title>',str(text))
    print(title[0])
