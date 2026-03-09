# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:

    def __init__(self):
        self.room = []

    def add(self, person: Person):
        self.room.append(person)

    def is_empty(self):
        if not self.room:
            return True
        return False
    
    def print_contents(self):
        total_height = 0
        for i in self.room:
            total_height += i.height

        print(f"There are {len(self.room)} persons in the room, and their combined height is {total_height} cm")

        for i in self.room:
            print(f"{i.name} ({i.height})")
            
    def shortest(self):
        if self.is_empty():
            return None
        
        shortest = self.room[0]

        for i in self.room:
            if i.height < shortest.height:
                shortest = i
        
        return shortest

    def remove_shortest(self):
        shortest_person = self.shortest()

        if shortest_person:
                return self.room.remove(shortest_person)
            
        return shortest_person
