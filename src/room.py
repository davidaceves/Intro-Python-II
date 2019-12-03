# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room: 
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        for item in self.items:
            return f'Current Room: {self.name} \nDescription: {self.description}\n{item}'

        # return f'Current Room: {self.name} \nDescription: {self.description}'