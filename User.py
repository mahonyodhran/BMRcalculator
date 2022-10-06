class User:
  def __init__(self, name, age, weight, height, gender):
    self.name = name
    self.age = age
    self.weight = weight
    self.height = height
    self.gender = gender
    
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r}, weight={self.weight!r}KG, height={self.height!r}CM, gender={self.gender!r})"