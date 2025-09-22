class Warrior:
    def __init__(self):
        self.health = 50
        self.attack_points = 5

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        enemy.take_damage(self.attack_points)

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack_points = 7


def fight(unit_1, unit_2):
    while True:
        unit_1.attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.attack(unit_1)
        if not unit_1.is_alive:
            return False
