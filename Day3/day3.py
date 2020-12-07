from functools import reduce

class Course():

    course = []
    line_length = None

    def __init__ (self):
        with open('challenge.txt','r') as f:
            for line in f:
                line = line.rstrip()
                self.course.append(list(line))
                if self.line_length != len(line) and self.line_length != None:            
                    print("Variable line length. Prev: %s, Current: %s" % (self.line_length, len(line)))
                    exit(1)
                self.line_length = len(line)

    def get_point(self, point):
        row = point[0]
        col = point[1]
        
        if row >= len(self.course):             
            return None

        return self.course[row][col % self.line_length]

def run_scenario(rightSteps, downSteps, course):
    TREES_HIT= 0    
    CurrentPoint = (0,0)
    
    while True:    
        point = course.get_point(CurrentPoint)
        if point == "#":
            TREES_HIT += 1
        elif point == ".":
            pass
        elif point == None:
            print("Right %s, Down %s. Trees Hit: %s" % (rightSteps, downSteps, TREES_HIT))
            return TREES_HIT            
        else:
            print("Shouldn't get here..")
            exit(1)
        row, col = CurrentPoint
        CurrentPoint = (row+downSteps, col+rightSteps)

scenarios = [(1,1), (3,1), (5,1), (7,1), (1,2)]
course = Course()

print("Part 1 Answer: %s" %(run_scenario(3,1,course)))

results = []
for i in scenarios:
    results.append(run_scenario(i[0],i[1],course))

print("Part 2 Answer: %s" %(reduce(lambda x, y: x*y, results)))