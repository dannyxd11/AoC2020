import re
import operator

class Ship():
    
    def __init__(self):
        self.position = (0,0)
        self.facing = "E"
        pass

    def manhattan_distance(self):
        return sum([abs(x) for x in self.position])

    def move(self, action, steps):
        action = self.facing if action == "F" else action
        x = (1 if action == "E" else -1 if action == "W" else 0) * steps
        y = (1 if action == "N" else -1 if action == "S" else 0) * steps
        self.position = tuple(map(operator.add, self.position, (x, y)))        

    def rotate(self, action, degrees):
        lookup = {"N": 0, "E": 1, "S": 2, "W": 3}
        rlookup = {0: "N", 1: "E", 2: "S", 3: "W"}
        rotation = (1 if action == "R" else -1) * (degrees / 90)
        self.facing = rlookup[(lookup[self.facing] + rotation) % 4]
        
    def act(self, action):
        match = re.match('([NEWSFRL])(\d+)', action)        
        action = match.group(1)
        steps = int(match.group(2))

        if action in ["N", "E", "S", "W", "F"]:
            self.move(action, steps)
        elif action in ["R", "L"]: 
            self.rotate(action, steps)

        return (self.position, self.facing)

route = []
with open ('challenge.txt', 'r') as f:
    route = [move.strip() for move in f.readlines()]

ship = Ship()
movements = [ ship.act(movement) for movement in route ]
print("[Part 1] Current Position: %s, Manhattan Distance: %s" % (ship.position, ship.manhattan_distance())) 