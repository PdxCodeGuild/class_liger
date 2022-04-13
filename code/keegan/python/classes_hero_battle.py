import time 

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} - Damage: {self.damage}"

# Character is the "base" class, which means other classes will be able to inherit
# the Character class' attribute through class inheritance
class Character:
    def __init__(self, name, weapon=None, hp=100):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        
    def is_defeated(self):
        '''Return True if the character's HP is <= 0, otherwise False'''
        return self.hp <= 0

    def attack(self, opponent):
        '''Subtract the character's weapon's damage rating from the opponent's hp
        Return a boolean indicating if the opponent is defeated'''
        print(f'\n{self.name} cries, "{self.battle_cry()}" and attacks!')

        weapon_damage = self.weapon.damage
        opponent.hp -= weapon_damage

        print(f"\n{self.name} does {self.weapon.damage} damage with their {self.weapon.name}!")
        print(f"{opponent.name} has {opponent.hp} HP remaining!")

        return opponent.is_defeated()



    def __str__(self):
        return f"Name: {self.name}, weapon: {self.weapon}, hp: {self.hp}"

# Hero inherits all the attributes from the Character class
class Hero(Character):
    def __init__(self, name, weapon=None, hp=100):
        # initial the Character class within the Hero class
        super().__init__(name, weapon, hp)

    
    def battle_cry(self):
        return 'I will defeat all evil!'


class Villain(Character):
    def __init__(self, name, weapon=None, hp=100):
        # initial the Character class within the Villain class
        super().__init__(name, weapon, hp)

    
    def battle_cry(self):
        return 'I will conquer the universe!'


def main():
    # create weapons
    great_sword = Weapon('Greatsword', 30)
    bow_n_arrow = Weapon('Longbow', 45)

    # create characters
    hero = Hero('Chronos', weapon=great_sword)
    villain = Villain('Helios', weapon=bow_n_arrow)

    # collect the fighters into a list to decide whose turn it is
    fighters = [hero, villain]

    turn = 0 # too keep track of whose turn it is
    while True:

        # 1.5 second pause
        time.sleep(1.5)

        # % 2 will always result in 0 or 1
        attacker = fighters[turn % 2]
        opponent = fighters[(turn + 1) % 2]

        # have the attacker attack the opponent
        battle_is_over = attacker.attack(opponent)

        # check if the opponent is defeated
        if battle_is_over:
            print(f"{opponent.name} is defeated, {attacker.name} is victorious!")
            break

        turn += 1


if __name__ == '__main__':
    main()