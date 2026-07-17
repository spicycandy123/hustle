import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0
        


    def battle(self, opponent):
        print(random.choice([self.name, opponent.name]))
    



if __name__== "__main__":
    my_hero = Hero("Hulk", 150)
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("Thanos", 200)
    my_hero.battle(my_opponent)
