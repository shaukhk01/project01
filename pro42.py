import re,urllib
import urllib.request
def main():
    site = "google rediff".split()
    print(site)
    for s in site:
        print('searching.....',s)
        u = urllib.request.urlopen("http://"+s+".com")
        text = u.read()
        title = re.findall('<title>.*</title>',str(text))
        print(title[0])
main()

