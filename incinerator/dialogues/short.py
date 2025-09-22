VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.history = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        return '\n'.join([f'{name} said: {msg}' for name, msg in self.history])

    def show_robot_dialogue(self):
        return '\n'.join([f'{name} said: {self.to_bin(msg)}' for name, msg in self.history])

    def to_bin(self, msg):
        return ''.join(map(lambda c: '0' if c in VOWELS else '1', msg.lower()))


class Human:
    def __init__(self, name=''):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.history.append((self.name, message))


class Robot:
    def __init__(self, serial_number=''):
        self.serial_number = serial_number
        self.chat = None

    def send(self, message):
        self.chat.history.append((self.serial_number, message))
