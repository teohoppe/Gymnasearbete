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

print(f"Delta V needed: {total_delta_v}")

class Engine:
    def __init__(self, weight, exhaust_v) -> None:
        self.weight = weight
        self.exhaust_v = exhaust_v

class Rocket:
    def __init__(self, speed, fuel, mass, engine, delta_v):
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.engine = engine
        self.delta_v = delta_v

    def calc_fuel_needed_and_delta_v(self):
        self.mass += self.engine.weight
        
        # delta v input
        delta_v_input = int(input("How much delta V do you want:  "))
        
        # Clalc fuel needed
        self.fuel = ((math.e ** ((delta_v_input/self.engine.exhaust_v))) * self.mass) - self.mass 
        
        # clalc delta v
        self.delta_V = self.engine.exhaust_v * math.log((self.mass + self.fuel) / self.mass)
        
        print(f"fuel needed: {self.fuel} kg")
        print(f"delta V given {self.delta_V} m/s")
        
        return self.delta_V, self.fuel

RS_25_Engine = Engine(2390, 232375*10)

# https://www.spaceflightinsider.com/hangar/falcon-9/
SpaceX_Merlin = Engine(470, 3050)

rocket = Rocket(10, 0, 3900, SpaceX_Merlin, 0)

rocket.calc_fuel_needed_and_delta_v()