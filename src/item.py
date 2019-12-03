class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Name: {self.name} \nDescription: {self.description}'

class Gold(Item): 
    def __init__(self, value):
        super().__init__('Gold', "It shines")
        self.value = value

    def __str__(self):
        return f'Gold: {self.value}'

