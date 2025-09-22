class Warrior(object):
    def __init__(self, health=50, attack_points=5):
        self.health = health
        self.attack_points = attack_points

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        enemy.take_damage(self.attack_points)

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack_points=7)


def fight(unit_1, unit_2):
    while True:
        unit_1.attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.attack(unit_1)
        if not unit_1.is_alive:
            return False


class Army(object):
    def __init__(self):
        self.units = []

    def add_units(self, unit, qty):
        for i in range(qty):
            self.units.append(unit())


class Battle(object):
    def fight(self, army_1, army_2):
        while army_1.units and army_2.units:
            if fight(army_1.units[0], army_2.units[0]):
                del army_2.units[0]
            else:
                del army_1.units[0]
        return len(army_2.units) == 0
