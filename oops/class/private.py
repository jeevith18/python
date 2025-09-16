class Fruit:
  def __init__(self,name:str,vitamin:str):
    self.name = name
    self.__vitamin = vitamin
    
  def print_fruit_vitamin(self):
    return f'the fruit is {self.name} and the vitamin is {self.__vitamin}'
  

fruit1 = Fruit('guava',"C")
print(fruit1.print_fruit_vitamin())

''' This will not work since it is a private variable'''
print(fruit1.__vitamin)

'''If you really want to do it, then this is the way but not recommended '''
print(fruit1._Fruit__vitamin)
