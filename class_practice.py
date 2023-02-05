class Circle: #create class
  pi = 3.14 # define class variable
  def area(self, radius):
    area = self.pi * radius ** 2 # define class method to calculate area with given radius and class variable (self.pi)
    return area
circle = Circle() # create instance of class
pizza_area = circle.area(12/2) # use class instance and method to calculate area of 12-inch pizza
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
