import math

# https://web.archive.org/web/20070701211813/http://www.pma.caltech.edu/~chirata/deltav.html

# Trans lunar ijection = TLI
# Mid Course Correction = MCC
# Lunar Orbit Insertion => enter lunar orbit = LOI
# Transfer Orbit = GTO
# Lunar Orbit = LO
# Lunar Surface = LS
# Dubbelkolla GTO
# Delta_V to LOE to LO = 3900

orbit_and_delta_v_moon = {"LEO": 9700, "TLI": 3150, "MCC": 500,
                     "LOI": 350, "GTO": 3200, "LO": 700, "LS": 1600}

total_delta_v = sum(orbit_and_delta_v_moon.values())

# Delta_V to LOE to LO = 3900 + MCC
total_delta_v_from_orbit = 3900 + 500

print(f"Delta V needed from LEO: {total_delta_v_from_orbit}")

class Engine:
    def __init__(self, weight, exhaust_v, ISP, flow_rate, trusth) -> None:
        self.weight = weight
        self.exhaust_v = exhaust_v
        self.ISP = ISP
        self.flow_rate = flow_rate
        self.trusth = trusth

class Rocket:
    def __init__(self, speed, fuel, mass, engine, delta_v, sum_exhaust_v):
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.engine = engine
        self.delta_v = delta_v
        self.sum_exhaust_v = sum_exhaust_v

    def calc_fuel_and_delta_v(self):
        self.mass += self.engine.weight
        
        # delta v input
        delta_v_input = int(input("How much delta V do you want:  "))

        # Clalc fuel needed
        self.fuel = math.ceil(((math.e ** ((delta_v_input/self.engine.exhaust_v))) * self.mass) - self.mass)

        # clalc delta v
        self.delta_V = self.engine.exhaust_v * \
            math.log((self.mass + self.fuel) / self.mass)

        print(f"fuel needed: {self.fuel} kg")
        print(f"delta V given {round(self.delta_V)} m/s")

        return self.delta_V, self.fuel

    def fuel_expense(self):
        # https://spaceimpulse.com/2023/06/13/how-much-does-rocket-fuel-cost/
        # RP-1 presents a cheaper option at $2.3/kg.
        # while LOX comes in at $0.27/kg
        # https://link.springer.com/chapter/10.1007/978-0-387-09630-8_4 STATES RATIO (2.27:1 mixture ratio of LOX to RP-1)

        sum_ratio = 2.27 + 1
        part_of_fuel = self.fuel / sum_ratio

        LOX_fuel = part_of_fuel * 2.27
        RP_1_fuel = part_of_fuel * 1

        LOX_fuel_price = LOX_fuel * 0.27
        RP_1_fuel_price = RP_1_fuel * 2.3

        total_fuel_price_in_dollars = round(LOX_fuel_price + RP_1_fuel_price)

        print(total_fuel_price_in_dollars)


# https://www.spaceflightinsider.com/hangar/falcon-9/
# SpaceX_Merlin flowrate is 140 kg/s, to calc change in exhous velocity
SpaceX_Merlin = Engine(470, 3050, 342, 140, 981000)

rocket = Rocket(10, 0, 3900, SpaceX_Merlin, 0, 0)

rocket.calc_fuel_and_delta_v()
rocket.fuel_expense()
