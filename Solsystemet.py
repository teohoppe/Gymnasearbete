jorden = {'mass': 5.972 * 10**24, 'radie': 6371 * 1000, 'g': 9.82}
moon = {'mass': 7.35 * 10**24, 'radie': 1737.4 * 1000, 'g moon': 1.62}


class Planet:
    def __init__(self, mass, radius, g):
        self.mass = mass
        self.radius = radius
        self.g = g


moon = Planet(7.35 * 10**24, 1737.4 * 1000, 1.62)
earth = Planet(5.972 * 10**24, 6371 * 1000, 9.82)
