from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_1() 
    # Any code you write here will run before the form opens.
  
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    