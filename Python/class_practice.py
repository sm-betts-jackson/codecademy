class Circle: #create class
  pi = 3.14 # define class variable
  def area(self, radius):
    area = self.pi * radius ** 2 # define class method to calculate area with given radius and class variable (self.pi)
    return area
circle = Circle() # create instance of class
pizza_area = circle.area(12/2) # use class instance and method to calculate area of 12-inch pizza
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
class Student: # create a class - Student
  def __init__(self, name, year): # define a constructor that takes args - name & year
    self.name = name
    self.year = year
    self.grades = []    # add empty list - grades
  def add_grade(self,grade): # define a method - add_grade - that intakes arg - grade
    if type(grade) == Grade: # ensure grade is the type of class - Grade
      self.grades.append(grade) # add grade to list of grades
  def get_average(self): # define method - get_average 
    average = 0
    if len(self.grades) > 1:
      for score in self.grades:
        sc = score.grade() # had to add grade method to Grade to return integer grade
        average += sc
      average /= len(self.grades)
    elif len(self.grades) == 1:
      average = self.grades[0].grade()
    return average

class Grade: # create a class - Grade
  minimum_passing = 65 # instance variable
  def __init__(self,score): # define a constructor that takes arg - score
    self.score = score
  def is_passing(self): # define a method - is_passing
    if self.score >= self.minimum_passing: # check if score is greater than the instance variable - minimum_passing
      return True
    else:
      return False
  def grade(self): # method created for Student.get_average()
    return self.score

roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(89))
print(pieter.get_average())
