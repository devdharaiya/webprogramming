import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
counts = 1

while counts <= 3:
    url = urllib.request.urlopen(soup('a')[2].get('href', None), context=ctx).read()
    soup = BeautifulSoup(url, 'html.parser')
    counts = counts + 1

print(soup('a')[2].contents[0])