import urllib,re
import urllib.request
sites = 'yahoo rediff'.split()
print(sites)
for list in sites:
    print('searching..',list)
    u = urllib.request.urlopen("http://"+list+".com")
    text = u.read()
    title = re.findall('<title>.*</title>',str(text))
    print(title)
