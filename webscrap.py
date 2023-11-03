import urllib2_file
from bs4 import BeautifulSoup

url = "https://www.myntra.com/towel-set/spaces/-spaces-set-of-6-grey--coral-solid-cotton-towel-set/18355110/buy"
page = urllib2_file.__url__(url)

a = BeautifulSoup(page)

print(a.prettify)

