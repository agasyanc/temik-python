class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 10
        #print("create character: " + self.name)

class Room:
    def __init__(self):
        self.name = "cds"
        #print("Room!")

class Game:
    def __init__(self):
        r = 4
        player = Character('Art')
        rooms = []
        for a in range(r):
            row = []
            for b in range(r):
                room = Room()
                row.append(room)
            rooms.append(row)
        print(rooms)
        
game = Game() 

























































