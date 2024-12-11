from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def button_1_click(self, **event_args):
    """This method is called when the CSS3 button is clicked"""
    print("CSS3 Button clicked!")
    # Add any functionality you want for button 1

  def button_2_click(self, **event_args):
    """This method is called when the HTML5 button is clicked"""
    print("HTML5 Button clicked!")
    # Add any functionality you want for button 2
