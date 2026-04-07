import random

class Character:
    def __init__(self):
        for ability in ["strength", "dexterity", "constitution",
                        "intelligence", "wisdom", "charisma"]:
            nums = [random.randint(1, 6) for _ in range(4)]
            nums.remove(min(nums))
            setattr(self, ability, sum(nums))

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return random.choice([
            self.strength, self.dexterity, self.constitution,
            self.intelligence, self.wisdom, self.charisma
        ])
 

def modifier(value):
    return (value - 10) // 2

