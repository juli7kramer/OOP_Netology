class Character:
    def __init__(self, name, power, energy=100, hands=2):
        # параметром по-умолчанию backpack делать не будем, чтобы он не был общим
        self.name = name
        self.power = power
        self.energy = energy
        self.backpack = [] # будем присваивать пустой список именно для КОНКРЕТНОГО экземпляра при создании (self)
        self.hands = hands

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')        
    
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')
    
    def change_alias(self, new_alias):
        self.alias = new_alias
        

peter = Character("Peter Parker" , 80)
print(peter.name)
print(peter.power)
print(peter.hands)

print(peter.__dict__)
print(Character.__dict__)

bruce = Character("Batman" , 90)
print(bruce.__dict__)

peter = Character("Peter Parker" , 80)
peter.backpack.append("Web-shooters")
print(peter.backpack)
print(bruce.backpack)

