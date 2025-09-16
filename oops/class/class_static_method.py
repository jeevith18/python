class Fruit:
  def __init__(self,name:str,calorie:int):
    self.name = name
    self.calorie = calorie
    
  @staticmethod
  def cutFruit():
    print("static method")
    
  @classmethod
  def newFruit(cls, name:str, calorie:int):
    return cls(name,calorie)
  