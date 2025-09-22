class Friends:
    def __init__(self, connections):
        self.connections = {}
        for conn in connections:
            self.add(conn)

    def add(self, connection):
        m1, m2 = connection
        if m1 in self.connections and m2 in self.connections[m1]:
            return False
        if m1 not in self.connections:
            self.connections[m1] = set()
        if m2 not in self.connections:
            self.connections[m2] = set()
        self.connections[m1].add(m2)
        self.connections[m2].add(m1)
        return True

    def remove(self, connection):
        m1, m2 = connection
        if m1 in self.connections and m2 in self.connections[m1]:
            self.connections[m1].remove(m2)
            self.connections[m2].remove(m1)
            return True
        return False

    def names(self):
        return set([m for m in self.connections.keys() if len(self.connections[m]) > 0])

    def connected(self, name):
        return self.connections[name] if name in self.connections else set()
