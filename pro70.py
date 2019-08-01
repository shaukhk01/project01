import urllib,re
import urllib.request

def main():
    sites = "google rediff".split()
    for s in sites:
        print('searching....',s)
        u = urllib.request.urlopen("http://"+s+".com")
        text = u.read()
        title = re.findall('<title>.*</title>',str(text))
        print(title[0])
main()
