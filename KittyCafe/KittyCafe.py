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
kitty_cafe = '''
      |  /                       ____                  /
      | /  * ----- ----- \   /  /    \    ^    ____  ____  |
      |:   |   |     |    \ /   !        / \   |     |     |
      | \  |   |     |     |    !       /---\  |==   |==   |
      |  \ |   |     |     |    \____/ /     \ |     |___  o
      
      ''' 
kitty_images = [teeny_tiny,small,fluffy,chonky,hekkin_big,ENORMOUS]
life = 3 
instructions = ['''
Since you're a new worker here at KittyCafe, 
it's time to learn how it all works...
''', '''
As each cat enters the KittyCafe, you will learn it's
size, name, hunger level, and favorite food.
''','''
It's important that our kitty customers leave the restaurant satisfied,
so try to remember each cat's favorite food when cooking.
Cats may have 9 lives, but you only have 3!
''']
def intro(kitty_images,kitty_cafe,instructions):
    print('                           WELCOME TO')
    print(kitty_cafe)
    input('Press ENTER...')
    input(instructions[0])
    input("Our guests come in all shapes and sizes...\n")
    input('From teeny tiny...\n'+kitty_images[0])
    input('to fluffy...\n'+kitty_images[2])
    input('to absolutely ENORMOUS!!!\n'+kitty_images[-1])
    input("They are all quite hungry, and can't wait to eat!") 
    for rule in instructions[1:]:
        input(rule)
    print('Time to get started!!!\n')
    input('Press ENTER...\n')

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
        print(kitty_images[kitty_size_idx])
        time.sleep(1)
        if self.kitty_size == "ENORMOUS":
            print('An {size} kitty named {name} has entered your cafe!'.format(
                size=self.kitty_size, name=self.kitty_name))
        else:
            print('A {size} kitty named {name} has entered your cafe!'.format(
                size=self.kitty_size, name=self.kitty_name))
        time.sleep(1) 
        print("{name}'s favorite food is *{fave}*.".format(
                name=self.kitty_name, fave=self.kitty_favorite))
        time.sleep(1)
        print("It looks like {name} is {sat}".format(
                name=self.kitty_name,sat=self.current_sat))
        time.sleep(1)
        print('Better get cooking!')
        time.sleep(2)
    def feed_kitty(self,choice1,choice2,food):
        time.sleep(1)
        print('You served {food} to {name}.\n'.format(
                food=food,name=self.kitty_name))
        time.sleep(1)
        if choice1 == self.kitty_favorite or choice2 == self.kitty_favorite:
            current_sat_idx = -1
            current_sat = self.sat_levels[current_sat_idx]
            print("Excellent! {name} is {sat}\n".format(
                    name=self.kitty_name,sat=current_sat))
            time.sleep(1)
            print('Thanks for feeding {name}!\n'.format(name=self.kitty_name))
            time.sleep(1)
            update = input("Will you feed the next cat?\n(Y/N)\n")
            fave = True
        if choice1 != self.kitty_favorite and choice2 != self.kitty_favorite:
            if self.size_list.index(self.kitty_size) < self.size_list.index("fluffy"):
                current_sat = self.sat_levels[2]
                print("It looks like {name} is still {sat}\n".format(
                        name=self.kitty_name,sat=current_sat))
            elif self.size_list.index(self.kitty_size) >= self.size_list.index("fluffy"):
                current_sat = self.sat_levels[-2]
                print("It looks like {name} is still {sat}\n".format(
                        name=self.kitty_name, sat=current_sat))
            time.sleep(1)
            update = input("Will you feed it more?\n(Y/N)\n")
            fave = False
        return update, fave
                
def print_options(options):
    for opt in options:
        print(opt)
        if opt == options[-2]:
            print('or')
        if opt == options[-1]:
            choice = input('???\n')
    return choice

def print_choice(choice,options,meals):
    for i,pick in enumerate(options):
        if choice == pick:
            food = meals[i]
            return food 
    
class Cafe:
    ingredients = ['milk','mice','tuna','quail']  
    def cook(self):
        time.sleep(1)
        print("You have these ingredients to start with:\n")
        time.sleep(1)
        for ingredient in self.ingredients:
            print("*{}*".format(ingredient))
            time.sleep(0.5)
        choice1 = input("\nWhich would you like to add?")
        time.sleep(1)
        print("\nGreat! What else would you like to add?")
        if choice1 == 'milk':
            options = ['catnip', 'tuna', 'mice', 'nothing']
            meals = ['catnip tea', 'a tuna milkshake', 'a mouse float', 'warm milk']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        elif choice1 == 'mice':
            options = ['butter', 'flour','milk', 'nothing']
            meals = ['buttered mice', 'fried mice', 'a mouse float', 'mouse a la carte']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        elif choice1 == 'tuna':
            options = ['milk','flour','nothing']
            meals = ['a tuna milkshake', 'tuna patties', 'tuna a la carte']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        elif choice1 == 'quail':
            options = ['butter','milk','flour','nothing']
            meals = ['buttered quail', 'birdie breakfast', 'fried chicken', 'quail a la carte']
            choice2 = print_options(options)
            food = print_choice(choice2,options,meals)
        else:
            print('You do not have that ingredient!')
            food = "nothing"
        time.sleep(2)
        print("\nYou've made {}!\n".format(food))
        return choice1, choice2, food

# In[] 
lives = 3
intro(kitty_images,kitty_cafe,instructions)   
cat = Kitty()
cat.generate_kitty()
cafe = Cafe()
choice1, choice2, food = cafe.cook()
update, fave = cat.feed_kitty(choice1,choice2,food)
#True,Y --> new cat
#True,N --> end game
#False, Y --> feed cat again
#False, N --> lose game
while lives >= 1:
    print('UPDATE',update,'FAVE',fave)
    if fave == True:
        if update == 'Y':
            cat = Kitty()
            cat.generate_kitty()
            cafe = Cafe()
            choice1, choice2, food = cafe.cook()
            update, fave = cat.feed_kitty(choice1,choice2,food)
        elif update == 'N':
            print("Thank you for serving at\n")
            print(kitty_cafe)
    elif fave == False:
        if update == 'Y':
            choice,food = cafe.cook()
            update, fave = cat.feed_kitty(choice,food)
        elif update == 'N':
            lives -= 1
            if lives > 0:
                print('\nYou made {name} angry!!! =^.v.^='.format(name = cat.kitty_name))
                print('''
  ^ v ^ 
(= *^* =)
        ''')
                print("Better be more careful next time!")
if lives == 0:
    print(''' 
                  You're
           _____  
           |      _  ___  _
           |_  * |_) |   |  \  |
           |   | |\  |=  |   ) |
           |   | | \ |__ |_ /  *
           ''')
    
    

# In[]


