class KittyCafe:
    # to create a kitty, give it a name, type, and level. Its max fullness is determined by its level. Its starting satisfaction is 0, and it is hangry when it starts.
    def __init__(self, name, typ, size,satisfaction=0):
        self.name = name
        self.typ = typ
        self.size = size
        self.satisfaction = satisfaction
        self.max_satisfaction = 5
    def __repr__(self):
        # printing a kitty will tell you it's information
        return "This kitty, {name} is {size} and {satisfaction}"
    


size = {4:"ENORMOUS", 3: "hekkin big", 2:"chonky", 1:"fluffy", 0:"teenie"}
satisfaction = {
        0: "about to claw your eyes out!",
        1:"hangry",
        2:"super hungry",
        3:"hankering for some food",
        4:"needs a snack",
        5:"satisfied & purring"}

class Feed:
    pass
