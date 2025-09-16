from abc import abstractmethod, ABC


class Bike(ABC):
  def __init__(self, name, model, color):
    self.name = name
    self.model = model
    self.color = color
  
  @abstractmethod
  def getPetrol(self):
    return f'Petrol filled'
  
class Honda(Bike):
  def __init__(self, name, model, color):
    super().__init__(name, model, color)
  
  def getPetrol(self):
    return f'Petrol filled'


hornet:Honda = Honda('Hornet','160', 'black')
print(hornet.getPetrol())
