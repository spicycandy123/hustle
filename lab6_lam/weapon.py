import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        
        half_damage = int(self.max_damage) // 2
        random_damage = random.randint(half_damage, int(self.max_damage))
        
        print(random_damage)
        return random_damage

if __name__ == "__main__":
    weapon_1 = Weapon("Infinity Sword", 80)
    print(weapon_1.name)
    print(weapon_1.max_damage)
    weapon_1.attack()