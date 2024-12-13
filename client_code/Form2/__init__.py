from ._anvil_designer import Form2Template
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil import *

class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.markdown_input.text = ""  # Initialize empty markdown
    self.update_preview()
    
  def markdown_input_change(self, **event_args):
    """Triggered whenever the user types in the Markdown TextArea."""
    self.update_preview()
  def update_preview(self):
    """Send Markdown to the server and display the generated HTML."""
    markdown_content = self.markdown_input.text
    try:
      html_content = anvil.server.call('generate_html', markdown_content)
      self.html_preview.html = html_content
    except Exception as e:
      alert(f"Error updating preview: {e}")
  def export_button_click(self, **event_args):
    """Export the final HTML as a file."""
    markdown_content = self.markdown_input.text
    try:
        file = anvil.server.call('export_html', markdown_content)
        download(file)
    except Exception as e:
      alert(f"Error exporting HTML: {e}")
      

   