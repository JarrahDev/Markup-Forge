import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from bs4 import BeautifulSoup as BS4
import re

# Open and parse the HTML file
with open("_/theme/W3/JS.html", "r") as html_file:
    soup = BS4(html_file.read(), 'html.parser')

# Find all <script> tags
script_tags = soup.find_all('script')
listJS = []
# Extract and print JavaScript line by line
def displayJS(listJS):
  for script in script_tags:
    if script.string:  # Ensure the <script> tag contains text
        js_code = script.string.strip()
        js_lines = re.split(r'\n', js_code)  # Split code into lines using regex
        for line in js_lines:
          strpline = line.strip()  # Print each line after stripping extra whitespace
          print_lines = input("Do you want to print the JS lines? (Y/N)")
          if print_lines.strip().lower() == 'y' is True:  # Handle input correctly
                    print("Here is the JS Code:", strpline)
                listJS.append(strpline)  # Append line to list
            # Check if the list is successfully populated
            if listJS:
                print("Lines of code were successfully appended into the list!")
            else:
                print("No lines of code were added to the list.")
  displayJS()

