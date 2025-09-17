from typing import Protocol

class learnable(Protocol):
  def structured_syllabus(self):
    return "Syllabus!!"
  
class python():
  def structured_syllabus(self):
    return "python Syllabus!!"
  
class java():
  def structured_syllabus(self):
    return "java Syllabus!!"
  
def get_syllabus(interest:learnable):
  print(interest.structured_syllabus())
  
py: python = python()

get_syllabus(py)
