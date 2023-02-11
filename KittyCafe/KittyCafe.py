import random as rd
import numpy as np
import time

input('''
                           WELCOME TO
      |  /                       ____                  /
      | /  * ----- ----- \   /  /    \    ^    ____  ____  |
      |:   |   |     |    \ /   !        / \   |     |     |
      | \  |   |     |     |    !       /---\  |==   |==   |
      |  \ |   |     |     |    \____/ /     \ |     |___  o
      
                          Press ENTER...
      ''') 
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
print("Our guests come in all shapes and sizes...")
time.sleep(3)
print('From teeny tiny...\n'+teeny_tiny)
time.sleep(2)
print('to fluffy...\n'+fluffy)
time.sleep(2)
print('to absolutely ENORMOUS!!!\n'+ENORMOUS)
time.sleep(3)
input("They are all quite hungry, and can't wait to eat!\nPress ENTER...")
directions = """

"""
kitty_images = [teeny_tiny,small,fluffy,chonky,hekkin_big,ENORMOUS]

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
    def __init__(self): #currently needs no inputs bc names & sizes are randomly generated
    # The minimum food points needed to increase satisfaction are determined by its size. 
        pass
    def __repr__(self):
        pass
    def generate_kitty(self):
        self.kitty_name = self.name_list[rd.randint(0, len(self.name_list)-1)]
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
        input('''This {size} kitty's name is {name}, and
it looks like {name} is {sat}

Better get cooking!'''.format(
                size=self.kitty_size, name=self.kitty_name, sat=self.current_sat))
    
class Cafe:
    ingredients = ["milk", "roast", "flour", "mice", "catnip", "treats", 
                "tuna", "birds"]
#    menu = {"sass pancakes": "flour", 
#            "mouse dinner": "mice", 
#            "catnip tea": "catnip", 
#            "treat spread": "treats",
#            "tuna boat": "tuna",
#            "birdie breakfast": "birds",
#            "purrloin roast": "roast", 
#            "warm milk": "milk"}
    def cook(self):
        print("You have these ingredients:")
        time.sleep(1)
        for ingredient in self.ingredients:
            print("{}".format(ingredient))
            time.sleep(1)
        choice1 = input("Which would you like to add?\n")
        time.sleep(1)
        print("Great! Would you like to add something else?")
        
        if choice1 == 'milk':
            options = ['catnip', 'tuna', 'mice', 'nothing']
            meals = ['catnip tea', 'a tuna milkshake', 'a mouse float', 'warm milk']
            choice2 = input("{}, {}, {} or {}?\n".format(
                    options[0],options[1],options[2],options[3]))
            for i,pick in enumerate(options):
                if choice2 == pick:
                    food = meals[i]
        elif choice1 == 'mice':
            options = ['butter', 'flour','milk', 'nothing']
            meals = ['buttered mice', 'fried mice', 'a mouse float', 'mouse dinner']
            choice2 = input("{}, {}, {}, or {}?\n".format(
                    options[0],options[1],options[2],options[3]))
            for i,pick in enumerate(options):
                if choice2 == pick:
                    food = meals[i]
        return food
    def update_satisfaction(self):
        pass
# In[]    
kat = Kitty()
kat.generate_kitty()
cafe = Cafe()
time.sleep(2)
print("Time to add your first ingredient...")
time.sleep(2)
food = cafe.cook()
print("You've made {}!".format(food))

# In[]


