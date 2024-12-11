import anvil.server
from bs4 import BeautifulSoup as BS4
import re

# Open and parse the HTML file
with open("_/theme/W3/JS.html", "r") as html_file:
    soup = BS4(html_file.read(), 'html.parser')

# Find all <script> tags
script_tags = soup.find_all('script')
# Extract and print JavaScript line by line
def displayJS():
for script in script_tags:
    if script.string:  # Ensure the <script> tag contains text
        js_code = script.string.strip()
        js_lines = re.split(r'\n', js_code)  # Split code into lines using regex
        for line in js_lines:
            print(line.strip())  # Print each line after stripping extra whitespace
            

