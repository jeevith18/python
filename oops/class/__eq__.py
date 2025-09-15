class Bike:
  def __init__(self,company:str,name:str):
    self.company = company
    self.name = name
  
  '''
  The __eq__ method is called automatically when you use the == operator between two objects of the Bike class.
  In your code, print(bike1 == bike2) triggers bike1.__eq__(bike2), which compares their attributes using 
  self.__dict__ == other.__dict__.
  '''
  
  def __eq__(self, other):
    return (self.__dict__ == other.__dict__)
    
bike1:Bike = Bike('Bajaj','Pulsar')
#bike2:Bike = Bike('Bajaj','Pulsar')
bike2:Bike = Bike('Harley Davidson','Fat Boy')

print(bike1 == bike2)
