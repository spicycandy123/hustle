import random
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
     def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

     def create_ability(self):
        name = input("Ability name? ")
        max_damage = input("Max damage of the ability? ")
        return Ability(name, int(max_damage))

     def create_weapon(self):
        name = input("Weapon name? ")
        max_damage = input("Max damage of the weapon? ")
        return Weapon(name, int(max_damage))
        
     def create_armor(self):
        name = input("What is the armor name?  ")
        max_block = input("What is the max block of the armor?  ")
        return Armor(name, int(max_block))

     def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        
         #From here i did asked ai for help

        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            
            if add_item == "1":
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif add_item == "2":
                new_weapon = self.create_weapon()
                hero.add_weapon(new_weapon)
            elif add_item == "3":
                new_armor = self.create_armor()
                hero.add_armor(new_armor)
                
        return hero

     def build_team_one(self):
        team_name = input("What is the name of Team One? ")
        self.team_one = Team(team_name)
        
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

     def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input("What is the name of Team Two? ")
        self.team_two = Team(team_name)
        
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

     def team_battle(self):
        self.team_one.attack(self.team_two)

     def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_one_kills = 0
        team_one_deaths = 0
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_one_kills / team_one_deaths))

        team_two_kills = 0
        team_two_deaths = 0
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_two_kills / team_two_deaths))

        team_one_alive = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print("Survived from " + self.team_one.name + ": " + hero.name)
                team_one_alive += 1

        team_two_alive = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print("Survived from " + self.team_two.name + ": " + hero.name)
                team_two_alive += 1

        if team_one_alive > team_two_alive:
            print("\n*** " + self.team_one.name + " Wins! ***")
        elif team_two_alive > team_one_alive:
            print("\n*** " + self.team_two.name + " Wins! ***")
        else:
            print("\n*** It's a Draw! ***")

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()