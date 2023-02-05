# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  def __init__(self, input_name, input_breed, input_age = 0, input_cuddly = True, input_friends = []):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = input_cuddly
    self.friends = input_friends
  def __repr__(self):
      description = "{name} is a {breed} and is {age} years old. {name} has {number_of_friends} friends.".format(name = self.name, breed = self.breed, age=self.age, number_of_friends=len(self.friends))
      if self.is_cuddly:
        description += " {name} is a cuddly cat.".format(name = self.name)
      else:
        description += " {name} is a nasty cat.".format(name = self.name)
      return description
  # Create method where two
  # pets interact.
  # Ex: def name(self, pet):
  def cuddles(self, other_cat):
    if (other_cat.is_cuddly):
      self.friends.append(other_cat)
      other_cat.friends.append(self)
      print("{name} and {name2} are cuddling! Purr purr...".format(name = self.name, name2 = other_cat.name))
    else:
      print("{name2} is about to claw {name}'s eyes out!!! Help!".format(name2 = other_cat.name, name = self.name))
# Create two pets.
cat_one = Cat("Leo", "Maine Coon", 7, False)
cat_two = Cat("Scampers", "Tuxedo", 17, True)
print(cat_one.__repr__())
print(cat_two.__repr__())
# Call your method below.
cat_one.cuddles(cat_two)
cat_two.cuddles(cat_one)
