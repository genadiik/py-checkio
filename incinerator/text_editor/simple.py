class Text:
    def __init__(self):
        self.data = ''
        self.font = ''

    def write(self, text):
        self.data += text

    def set_font(self, font):
        self.font = font

    def show(self):
        return f'[{self.font}]{self.data}[{self.font}]'.replace('[]', '')

    def restore(self, state):
        self.data, self.font = state


class SavedText:
    def __init__(self):
        self.versions = []

    def save_text(self, text):
        self.versions.append((text.data, text.font))

    def get_version(self, number):
        return self.versions[number]
