#class Point():
#    def __init__(self, input1, input2):
#        self.x = input1
#        self.y = input2

#p = Point(2, 8)
#print(p.x)
#print(p.y)
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = [] # stores self.passengers to an empty list

    def add_passenger(self, name):
        if not self.open_seats(): #if statement whenever  not seats are available
            return False
        self.passenger.append(name)
        return True
        
    
    def open_seats(self):
        return self.capacity - len(self.passenger)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for that {person}")
    
