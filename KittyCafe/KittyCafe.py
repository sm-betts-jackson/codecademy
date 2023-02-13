import random as rd
import numpy as np
import time

teeny_tiny = r'''
 |\___/|
 | o o |
 \= ^ =/    
  )   (  ((
 /     \  ))
/||   ||\((
\||___||/_/
 '"   "'
'''
small = r'''
 |\_____/|
 |  o o  |
 \=  ^  =/
  )     (    
 /       \ ((
 |       |  ))
/| |   | |\((
\| |___| |/_/
 '"'   '"'
'''
fluffy = r'''
   /\^^^^^/\
  <  o . o  >
  < =  ^  = > \\
    )     (   //
   /       \  \\
  / |    |  \ //
((__|____|__))/
   ""      ""
 '''
chonky = r'''
    /\^^^^^/\
   <  o . o  >
   ( =  ^  = )  \\
    /       \   //
   (         )  \\
 ((  )    (  )) //
( (__)____(__)_)/
   ""      ""
'''
hekkin_big = r'''
    /\^^^^^/\
   /  o . o  \
  ( ==  ^  == )  \\
   )         (   //
  (           )  \\
 ( (  )   (  ) ) //
(__(__)___(__)__)/
    ""     "" 
'''
ENORMOUS = r'''
    /\^^^^^^^/\
   /  o  .  o  \
  ( ==   ^   == )  
   \           /   \\
   /           \   //
  (             )  \\
 ( (  )     (  ) ) //
(__(__)_____(__)__)/
    ""       ""
'''
kitty_images = [teeny_tiny,small,fluffy,chonky,hekkin_big,ENORMOUS]

def intro(kitty_images):
    input('''
                           WELCOME TO
      |  /                       ____                  /
      | /  * ----- ----- \   /  /    \    ^    ____  ____  |
      |:   |   |     |    \ /   !        / \   |     |     |
      | \  |   |     |     |    !       /---\  |==   |==   |
      |  \ |   |     |     |    \____/ /     \ |     |___  o
      
                          Press ENTER...
      ''') 

    print("Our guests come in all shapes and sizes...")
    time.sleep(3)
    print('From teeny tiny...\n'+kitty_images[0])
    time.sleep(2)
    print('to fluffy...\n'+kitty_images[2])
    time.sleep(2)
    print('to absolutely ENORMOUS!!!\n'+kitty_images[-1])
    time.sleep(3)
    input("They are all quite hungry, and can't wait to eat!\nPress ENTER...")
    directions = """

"""
# In[]
class Kitty:
    name_list = ["Leo", "Scampers", "Mittens", "Boots", "Charlie", "Buddy", 
                 "Moomoo", "Chichi", "Lola", "Honey", "Lilly", "Zoom", "Arnold",
                 "Sammy", "Jelly", "Butters","Willy","Precious","Max","Maple"]
    size_list = ["teeny tiny", "small", "fluffy", "chonky", "hekkin big", "ENORMOUS"]
    sat_levels = [
        "about to claw your eyes out!!!",
        "ravenous!",
        "hangry.",
        "in need of a snack...",
        "a bit peckish...",
        "satisfied & purring =^..^="
        ]
    favorites = ['milk','mice','tuna','quail']
    def __init__(self): #currently needs no inputs bc names & sizes are randomly generated
    # The minimum food points needed to increase satisfaction are determined by its size. 
        pass
    def __repr__(self):
        return("Generates a kitty & updates satisfaction levels.")
    def generate_kitty(self):
        self.kitty_name = self.name_list[rd.randint(0, len(self.name_list)-1)]
        self.kitty_favorite = self.favorites[rd.randint(0, len(self.favorites)-1)]
        self.kitty_size = self.size_list[rd.randint(0, len(self.size_list)-1)]
        kitty_size_idx = self.size_list.index(self.kitty_size)
        if kitty_size_idx > self.size_list.index("fluffy") and self.kitty_size != "ENORMOUS":
            current_sat_idx = 1 # the larger cats are hungrier
        elif kitty_size_idx <= self.size_list.index("fluffy") and self.kitty_size != "teeny tiny":
            current_sat_idx = 2
        elif self.kitty_size == "ENORMOUS":
            current_sat_idx = 0
        elif self.kitty_size == "teeny tiny":
            current_sat_idx = 3
        self.current_sat = self.sat_levels[current_sat_idx]
        print('A kitty has entered your cafe!')
        time.sleep(2) 
        print(kitty_images[kitty_size_idx])
        time.sleep(2)
        print("This {size} kitty's name is {name}.".format(
                size=self.kitty_size, name=self.kitty_name))
        time.sleep(2)
        print("It's favorite food is {fave}.".format(fave=self.kitty_favorite))
        time.sleep(2)
        print("It looks like {name} is \033[1m{sat}\033[0m".format(
                name=self.kitty_name,sat=self.current_sat))
        time.sleep(2)
        input('Better get cooking!')
    def feed_kitty(self,choice,food):
        print('You served {} to {}'.format(food,self.kitty_name))
        if choice == self.kitty_favorite:
            current_sat_idx = -1
            current_sat = self.sat_levels[current_sat_idx]
            print("Excellent! {name} is {sat}/n".format(
                    name=self.kitty_name,sat=current_sat))
        if choice != self.kitty_favorite:
            if self.size_list.index(self.kitty_size) < self.size_list.index("fluffy"):
                # still hungry
            else:
                # needs a little snack
            current_sat_idx = 
def print_options(options):
    for opt in options:
        print(opt)
        if opt == options[-2]:
            print('or')
        if opt == options[-1]:
            choice= input('???\n')
    return choice

def print_choice(choice,options,meals):
    for i,pick in enumerate(options):
        if choice == pick:
            food = meals[i]
    return food 
    
class Cafe:
    ingredients = ['milk','mice','tuna','quail']  
    def cook(self):
        time.sleep(2)
        print("Time to add your first ingredient...")
        time.sleep(2)
        print("You have these ingredients to start with:")
        time.sleep(1)
        for ingredient in self.ingredients:
            print("*{}*".format(ingredient))
            time.sleep(1)
        choice1 = input("Which would you like to add?\n")
        time.sleep(1)
        print("Great! What else would you like to add...")
        if choice1 == 'milk':
            options = ['catnip', 'tuna', 'mice', 'nothing']
            meals = ['catnip tea', 'a tuna milkshake', 'a mouse float', 'warm milk']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        elif choice1 == 'mice':
            options = ['butter', 'flour','milk', 'nothing']
            meals = ['buttered mice', 'fried mice', 'a mouse float', 'mouse dinner']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        elif choice1 == 'tuna':
            options = ['milk','flour','nothing']
            meals = ['a tuna milkshake', 'tuna patties']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        if choice1 == 'quail':
            options = ['butter','milk','flour','nothing']
            meals = ['buttered quail', 'birdie breakfast', 'fried chiken', 'quail a la carte']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        else:
            print('You do not have that ingredient!')
        return choice1, food
    def update_satisfaction(self):
        pass
# In[]  
#intro(kitty_images)        
kat = Kitty()
kat.generate_kitty()
cafe = Cafe()
choice, food = cafe.cook()
print("You've made {}!".format(food))

# In[]


