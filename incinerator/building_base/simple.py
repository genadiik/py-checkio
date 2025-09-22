class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self._width_we = width_WE
        self._width_ns = width_NS
        self._height = height
        self._corners = {
            'south-west': [south, west],
            'south-east': [south, west+width_WE],
            'north-east': [south+width_NS, west+width_WE],
            'north-west': [south+width_NS, west]
        }

    def corners(self):
        return self._corners

    def area(self):
        return self._width_we * self._width_ns

    def volume(self):
        return self.area() * self._height

    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(
            self._corners['south-west'][0],
            self._corners['south-west'][1],
            self._width_we,
            self._width_ns,
            self._height
        )
