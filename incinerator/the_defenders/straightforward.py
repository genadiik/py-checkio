class Warrior(object):
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def assault(self, enemy):
        if enemy.defense < self.attack:
            enemy.take_damage(self.attack - enemy.defense)

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self, health=60, attack=3, defense=2)


def fight(unit_1, unit_2):
    while True:
        unit_1.assault(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.assault(unit_1)
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
