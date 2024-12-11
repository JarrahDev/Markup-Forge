import anvil.server
from bs4 import BeautifulSoup as BS4

with open("_/theme/standard-page.html") as html:
  soup = BS4(html.read(), 'html.parser')
  tags = soup()
  




