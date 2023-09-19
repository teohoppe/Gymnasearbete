import math

# https://web.archive.org/web/20070701211813/http://www.pma.caltech.edu/~chirata/deltav.html

# Trans lunar ijection = TLI
# Mid Course Correction = MCC
# Lunar Orbit Insertion => enter lunar orbit = LOI
# Transfer Orbit = GTO
# Lunar Orbit = LO
# Lunar Surface = LS
# Dubbelkolla GTO

orbit_and_delta_v = {"LEO": 9700, "TLI": 3150, "MCC": 500,
                     "LOI": 350, "GTO": 3200, "LO": 700, "LS": 1600}

total_delta_v = sum(orbit_and_delta_v.values())

class Engine:
    def __init__(self, weight, thrust, fuel_com_per_sec) -> None:
        self.weight = weight
        self.thrust = thrust
        self.fuel_com_per_sec = fuel_com_per_sec
        
    

class Rocket:
    def __init__(self, speed, fuel, mass, engine):
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.engine = engine 

    def fuel_mass(self):
        fuel_mass = 1
        return self.fuel * fuel_mass

    def delta_v(self):
        delta_V = self.engine.thrust * math.log((self.mass + self.fuel_mass()) / self.mass)
        return delta_V
    
    def test(self):
        return self.engine.thrust

RS_25_Engine = Engine(2390, 232375*10, 999)

# https://www.spaceflightinsider.com/hangar/falcon-9/
SpaceX_Merlin = Engine(470, 981*10, 140)

rocket = Rocket(10, 10, 12, SpaceX_Merlin)

print(rocket.test())

print(rocket.delta_v())
