import random as rd
import numpy as np

input('''
                           WELCOME TO
      |  /                       ____                  /
      | /  * ----- ----- \   /  /    \    ^    ____  ____  |
      |:   |   |     |    \ /   !        / \   |     |     |
      | \  |   |     |     |    !       /---\  |==   |==   |
      |  \ |   |     |     |    \____/ /     \ |     |___  o
      
                          Press ENTER...
      ''')

class Kitty:
    name_list = ["Leo", "Scampers", "Mittens", "Boots", "Charlie", "Buddy", 
                 "Moomoo", "Chichi", "Lola", "Honey", "Lilly", "Zoom", "Arnold",
                 "Sammy", "Jelly", "Butters"]
    size_list = ["teeny tiny", "small", "fluffy", "chonky", "hekkin big", "ENORMOUS"]
    sat_levels = [
        "about to claw your eyes out!!!",
        "hangry af!",
        "super hungry.",
        "in need of a snack...",
        "a bit peckish...",
        "satisfied & purring =^.w.^="
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
        print('''A {size} kitty has entered your cafe!
The kitty's name is {name}.
It looks like {name} is {sat}
Better get cooking!'''.format(
                name=self.kitty_name, size=self.kitty_size, sat=self.current_sat))
    

kat = Kitty()
kat.generate_kitty()

  
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
    def __repr__(self):
        return '''
        Welcome to the KittyCafe!
        Here, you will be serving all sorts of kitties, cats, and meowing chonkers.
        Be careful; if they get too hungry, the claws will come out...
        But, if you feed them in a timely manner, you'll have a purring cuddle buddy!
        '''
    def cook(self):
        print("You have these ingredients:")
        for ingredient in self.ingredients:
            print("{}".format(ingredient))
        choice = input("Which would you like to add first?\n")
        print("You went with {}.".format(choice))
    def update_satisfaction(self):
        pass
cafe = Cafe()
cafe.cook()
show()
# In[]
class Feed:
    pass

teeny_tiny = '''
 |\___/|
 | o o |
 \= ^ =/    
  )   (  ((
 /     \  ))
/||   ||\((
\||___||/_/
 '"   "'
'''
small = '''
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
fluffy =  '''
    /\^^^^^/\
   <  o . o  >
   < =  ^  = > \\
     )     (   //
    /       \  \\
   / |    |  \ //
 ((__|____|__))/
   ""      ""
 '''
chonky = '''
    /\^^^^^/\
   <  o . o  >
   ( =  ^  = )  \\
    /       \   //
   (         )  \\
 ((  )    (  )) //
( (__)____(__)_)/
   ""      ""
'''
hekkin_big ='''
    /\^^^^^/\
   /  o . o  \
  ( ==  ^  == )  \\
   )         (   //
  (           )  \\
 ( (  )   (  ) ) //
(__(__)___(__)__)/
    ""     "" 
'''
ENORMOUS = '''
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