class fruit:
  def __init__(self, name: str, origin: str):
    """
    Initialize a fruit object with name and origin.
    Args:
      name (str): Name of the fruit.
      origin (str): Origin of the fruit.
    """
    self.name = name
    self._origin = origin

  @property
  def origin(self):
    """
    Get the origin of the fruit.
    Returns:
      str: The origin of the fruit.
    """
    print(f'private var is being accessed origin{self._origin}')
    return self._origin

  @origin.setter
  def origin(self, new_origin: str):
    """
    Set a new origin for the fruit.
    Args:
      new_origin (str): The new origin to set.
    """
    self._origin = new_origin
  
if __name__ == '__main__':
  papaya:fruit = fruit('papaya','india')
  print(papaya.name)
  papaya.origin='chennai'
  print(papaya.origin)