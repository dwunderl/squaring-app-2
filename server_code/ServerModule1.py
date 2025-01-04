import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

class SquaringStuff:
    def __init__(self, rootNumber=0):
        self.rootNumber = rootNumber
        self.squaredNumber = 0


    def squareProcess(self):
      self.squaredNumber = self.rootNumber**2
      fiftyDelta = self.rootNumber % 50
      if fiftyDelta > 25:
        fiftyDelta = fiftyDelta - 50
      middleSign = " + "
      if fiftyDelta < 0:
        middleSign = " - "
      fiftyBoundary = self.rootNumber - fiftyDelta
      firstSquared = (fiftyBoundary/10)**2
      firstCoeff = fiftyBoundary/100.0
      firstDoubledCoeff = int((fiftyBoundary/100.0)*2)
      middleTerm = firstDoubledCoeff * fiftyDelta
      lastSquared = fiftyDelta**2
      
      self.binomialExpression = "( " + str(fiftyBoundary) + middleSign + str(abs(fiftyDelta)) + " )^2^"
      self.expandedExpression1 = (str(int(fiftyBoundary/10)) + "^2^ (00)" + 
                                  middleSign + " 2 * " + str(firstCoeff) + " * " + str(abs(fiftyDelta)) + " (00) + " + 
                                  str(abs(fiftyDelta)) + "^2^")
      self.expandedExpression2 = (str(int(firstSquared)) + " (00)" + 
                                  middleSign + str(firstDoubledCoeff) + " * " + str(abs(fiftyDelta)) + " (00) + " + 
                                  str(lastSquared))
      self.columnAdditionExpression = str(int(firstSquared*100)) + "\n" + str(middleTerm*100) + "\n" + str(lastSquared)

    def get_attributes(self):
        return {'rootNumber': self.rootNumber, 
                'squaredNumber': self.squaredNumber, 
                'binomialExpression': self.binomialExpression,
                'expandedExpression1': self.expandedExpression1,
                'expandedExpression2': self.expandedExpression2,
                'columnAdditionExpression': self.columnAdditionExpression}


@anvil.server.callable
def say_hello(name):
  print("Hello, " + name + "!")
  return 42

@anvil.server.callable
def squareProcess(root):
  squaringStuff = SquaringStuff(root)
  squaringStuff.squareProcess()
  return squaringStuff.get_attributes()