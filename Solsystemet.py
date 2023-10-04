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
        self.delta_V = self.engine.exhaust_v * math.log((self.mass + self.fuel) / self.mass)
        
        print(f"fuel needed: {self.fuel} kg")
        print(f"delta V given {self.delta_V} m/s")
        
        return self.delta_V, self.fuel
    
    
    def exhaust_v_2(self):

        # LEtter to NASA
        # https://www.nasa.gov/content/submit-a-question-for-nasa/
        """I am working on a school project and was studying Tsiolkovsky's rocket equation. I was wondering how the total exhaust velocity in a rocket with multiple engines is calculated and how it would affect the rocket's total delta-v."""
        
        engine_amount = int(input("How many engines do you want: "))

        """engien_amount = int(input("How many engien do you want: "))
        self.sum_exhaust_v = ((self.engine.flow_rate * self.engine.ISP) * engien_amount) / (self.engine.flow_rate * engien_amount)
        return self.sum_exhaust_v"""
        
    
    def fuel_expense(self):
        
        # Fuel: RP-1 and liquid oxygen 
        # PR-1 11.34 KR per kilo
        # liquid oxygen 2.10 SEK per kilogram
        # 1 kg RP-1 needs 1.8 to 2.5 of LOX, mabye 2.15 
        # Assuem 1/3 kilo RP-1 = 2/3 Kilo LOZ  

        # THIS MIGHT BE WRONG
        # THIS IS WRONG
        rp_1_price = round((self.fuel/3) * (2.15/3),1)
        LOX_price =round((self.fuel*(2/3)) * (2.1 * (2/3)),1)
        
        total_fuel_price = rp_1_price + LOX_price
        
        print(total_fuel_price)
        



# https://www.spaceflightinsider.com/hangar/falcon-9/
# SpaceX_Merlin flowrate is 140 kg/s, to calc change in exhous velocity
SpaceX_Merlin = Engine(470, 3050, 342, 140, 981000)

rocket = Rocket(10, 0, 3900, SpaceX_Merlin, 0, 0)

rocket.calc_fuel_and_delta_v()
rocket.fuel_expense()
print("")
print(rocket.exhaust_v_2())