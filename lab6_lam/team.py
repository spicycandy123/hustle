import random
# i used ai for this because its confusing me, just a little support from ai.


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        print("Hero not found.")

    def view_all_heroes(self):
        
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / hero.deaths
            print(hero.name + " Kill/Deaths: " + str(kd))

    def revive_heroes(self):
        
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        
        living_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)

        
        living_opponents = []
        for opponent in other_team.heroes:
            if opponent.is_alive():
                living_opponents.append(opponent)

        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            
            hero.battle(opponent)

            
            if not hero.is_alive():
                living_heroes.remove(hero)
            if not opponent.is_alive():
                living_opponents.remove(opponent)