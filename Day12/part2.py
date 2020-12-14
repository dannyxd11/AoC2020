from math import cos, sin, pi
import operator
import re

class Ship():
    
    def __init__(self, **kwargs):
        self.position = (0, 0)    
        self.waypoint = (1, 1)

        if "waypoint" in kwargs.keys():
            self.waypoint = kwargs["waypoint"]
        if "position" in kwargs.keys():   
            self.position = kwargs["position"]

        pass

    def manhattan_distance(self):
        return sum([abs(x) for x in self.position])

    def move(self, action, steps):        
        if action == "F":
            x = self.waypoint[0] * steps
            y = self.waypoint[1] * steps
            self.position = tuple(map(operator.add, self.position, (x, y)))    
        else:            
            x = (1 if action == "E" else -1 if action == "W" else 0) * steps
            y = (1 if action == "N" else -1 if action == "S" else 0) * steps            
            self.waypoint = tuple(map(operator.add, self.waypoint, (x, y)))        

    def rotate(self, action, degrees):
        (x, y) = self.waypoint
        d = (degrees if action == "L" else -1 * degrees) * pi / 180                
        
        x1 = round(x * cos(d) - y * sin(d))
        y1 = round(x * sin(d) + y * cos(d))    

        self.waypoint = (x1, y1)  
        
    def act(self, action):
        match = re.match('([NEWSFRL])(\d+)', action)        
        action = match.group(1)
        steps = int(match.group(2))

        if action in ["N", "E", "S", "W", "F"]:
            self.move(action, steps)                    
        elif action in ["R", "L"]: 
            self.rotate(action, steps)

        return (self.position, self.waypoint)

route = []
with open ('challenge.txt', 'r') as f:
    route = [move.strip() for move in f.readlines()]

ship = Ship(waypoint = (10, 1))
movements = [ ship.act(movement) for movement in route ]
print("[Part 2] Current Position: %s, Manhattan Distance: %s" % (ship.position, ship.manhattan_distance())) 