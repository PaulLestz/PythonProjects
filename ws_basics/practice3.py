from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'lxml')

tbody = doc.tbody
trs = tbody.contents # .descendants # .children # ALMOST IDENTICAL?

'''

trs[1].previous_sibling # gets previous tag from same level

trs[0].next_sibling # gets next tag from same level

list(trs[0].next_siblings) # gets all next siblings in list form

list(trs[-1].previous_siblings) # gets all previous siblings in list form

trs[0].parent # gets tbody tag back (as can see above, .contents gives all children)

trs[0].parent.name == 'tbody' #TRUE

'''

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.text # .string == .text #TRUE
    fixed_price = price.a.text

    prices[fixed_name] = fixed_price

print(prices)