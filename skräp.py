import math

# Dictionary for delta_v values for various space missions
orbit_and_delta_v_moon = {
    "LEO": 9700, "TLI": 3150, "MCC": 500,
    "LOI": 350, "GTO": 3200, "LO": 700, "LS": 1600
}

# Class definitions for Engine and Rocket
class Engine:
    def __init__(self, weight, exhaust_v, ISP, flow_rate, trusth) -> None:
        self.weight = weight
        self.exhaust_v = exhaust_v
        self.ISP = ISP
        self.flow_rate = flow_rate
        self.trusth = trusth

class Rocket:
    def __init__(self, speed, fuel, mass, engine):
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.engine = engine
        self.delta_v = 0
        self.sum_exhaust_v = 0

    def calc_fuel_and_delta_v(self, desired_delta_v):
        self.mass += self.engine.weight
        self.fuel = math.ceil(((math.e ** (desired_delta_v / self.engine.exhaust_v)) * self.mass) - self.mass)
        self.delta_v = self.engine.exhaust_v * math.log((self.mass + self.fuel) / self.mass)
        print(f"Fuel needed: {self.fuel} kg")
        print(f"Delta V achievable: {round(self.delta_v)} m/s")
        return self.delta_v, self.fuel

    def fuel_expense(self):
        # RP-1/LOX for SpaceX Merlin
        if self.engine == "SpaceX Merlin":
            RP1_LOX_ratio = 2.27 + 1  # RP-1 to LOX ratio
            part_of_fuel = self.fuel / RP1_LOX_ratio
            LOX_fuel = part_of_fuel * 2.27
            RP1_fuel = part_of_fuel
            total_fuel_price_in_dollars = round(LOX_fuel * 0.27 + RP1_fuel * 2.3)

        # Methane/LOX for SpaceX Raptor
        elif self.engine == "Spacex Raptor":
            CH4_LOX_ratio = 3.6 + 1  # CH4 to LOX ratio
            part_of_fuel = self.fuel / CH4_LOX_ratio
            LOX_fuel = part_of_fuel * 3.6
            CH4_fuel = part_of_fuel
            total_fuel_price_in_dollars = round(LOX_fuel * 0.27 + CH4_fuel * 8.8)

        # LH2/LOX for RS-68
        elif self.engine == "RS-68":
            LH2_LOX_ratio = 5.97 + 1  # LH2 to LOX ratio
            part_of_fuel = self.fuel / LH2_LOX_ratio
            LOX_fuel = part_of_fuel * 5.97
            LH2_fuel = part_of_fuel
            total_fuel_price_in_dollars = round(LOX_fuel * 0.27 + LH2_fuel * 6.1)

        print(f"Total fuel price: ${total_fuel_price_in_dollars}")

# Function to select the engine based on user input
def select_engine():
    print("Select an engine:\n1. SpaceX Merlin\n2. SpaceX Raptor\n3. RS-68")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        return Engine(470, 3050, 342, 140, 981000)
    elif choice == '2':
        return Engine(1600, 3236, 350, 650, 2230000)
    elif choice == '3':
        return Engine(6600, 4464, 412, 550, 3370000)
    else:
        print("Invalid choice. Defaulting to SpaceX Merlin.")
        return Engine(470, 3050, 342, 140, 981000)

# Main Program
selected_engine = select_engine()
rocket = Rocket(10, 0, 3900, selected_engine)
desired_delta_v = int(input("How much delta V do you want: "))
rocket.calc_fuel_and_delta_v(desired_delta_v)
rocket.fuel_expense()
