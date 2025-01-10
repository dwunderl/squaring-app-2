from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def square_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.squaredNumber.text = str(int(self.rootNumber.text)**2)
    result = server.call('squareProcess',int(self.rootNumber.text))
    self.populateSquaringUI(result)
    pass

  def populateSquaringUI(self, squaringDict):
    self.squaredNumber.text = str(squaringDict['squaredNumber'])
    
    self.binomialExpression.content = squaringDict['binomialExpression']
    self.expandedExpression1.content = squaringDict['expandedExpression1']
    self.expandedExpression2.content = squaringDict['expandedExpression2']
    self.columnAdditionExpression.content = squaringDict['columnAdditionExpression']
    self.columnAdditionExpression2.content = squaringDict['columnAdditionExpression']