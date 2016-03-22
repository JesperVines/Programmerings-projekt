class Room:

    def __init__(self):

        self.name = ""
        self.description = ""
        self.north = ""
        self.east = ""
        self.south = ""
        self.west = ""
        self.picture

room_0 = Room
room_0.name = "Balcony"
room_0.description = "You are standing on a balcony. It's freezing outside."
room_0.north = None
room_0.east = None
room_0.south = 2
room_0.west = None

room_1 = Room
room_1.name = "Left wing"
room_1.description = "You are standing in the left wing of the house."
room_1.north = None
room_1.east = 2
room_1.south = 4
room_1.west = None

room_2 = Room
room_2.name = "Ball room"
room_2.description = "You are standing in a big ball room. Many parties have been held here."
room_2.north = 0
room_2.east = 3
room_2.south = 5
room_2.west = 1

room_3 = Room
room_3.name = "Right wing"
room_3.description = "You are standing in the right wing of the house."
room_3.north = None
room_3.east = None
room_3.south = 6
room_3.west = 2

room_4 = Room
room_4.name = "Bedroom"
room_4.description = "You are standing in a bedroom. There is only one big bed here."
room_4.north = 1
room_4.east = 5
room_4.south = None
room_4.west = None

room_5 = Room
room_5.name = "Dining Room"
room_5.description
