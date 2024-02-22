import math

# Map of delta_v values for space travel, source: https://web.archive.org/web/20070701211813/http://www.pma.caltech.edu/~chirata/deltav.html

# Abbreviations for different stages of lunar mission
# TLI: Trans Lunar Injection
# MCC: Mid Course Correction
# LOI: Lunar Orbit Insertion (enter lunar orbit)
# GTO: Geostationary Transfer Orbit
# LO: Lunar Orbit
# LS: Lunar Surface
# Note: Delta_V from Low Earth Orbit (LEO) to Lunar Orbit (LO) = 3900

# Dictionary mapping orbits to their respective delta_v values in m/s
orbit_and_delta_v_moon = {"LEO": 9700, "TLI": 3150, "MCC": 500,
                          "LOI": 350, "GTO": 3200, "LO": 700, "LS": 1600}

# Calculate total delta_v for all stages
total_delta_v = sum(orbit_and_delta_v_moon.values())

# Total delta_v from Low Earth Orbit to Lunar Orbit including MCC
total_delta_v_from_orbit = 3200 + 700 + 1600

print(f"Delta V needed from LEO: {total_delta_v_from_orbit}")


class Engine:
    """Represents a rocket engine with various parameters."""

    def __init__(self, weight, exhaust_v, ISP, flow_rate, thrust) -> None:
        self.weight = weight
        self.exhaust_v = exhaust_v
        self.ISP = ISP
        self.flow_rate = flow_rate
        self.thrust = thrust


class Rocket:
    """Represents a rocket with attributes like speed, fuel, mass, and engine."""

    def __init__(self, speed, fuel, mass, engine, delta_v, sum_exhaust_v):
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.engine = engine
        self.delta_v = delta_v
        self.sum_exhaust_v = sum_exhaust_v

    def calc_fuel_and_delta_v(self):
        """Calculates the fuel needed and the resulting delta_v based on engine efficiency."""
        self.mass += self.engine.weight

        # User input for desired delta_v
        delta_v_input = int(input("How much delta V do you want:  "))

        # Calculate fuel needed using the rocket equation
        self.fuel = math.ceil(
            (math.exp(delta_v_input / self.engine.exhaust_v) * self.mass) - self.mass)

        # Calculate achievable delta_v with the added fuel
        self.delta_v = self.engine.exhaust_v * \
            math.log((self.mass + self.fuel) / self.mass)

        print(f"Fuel needed: {self.fuel} kg")
        print(f"Delta V achieved: {round(self.delta_v)} m/s")

        return self.delta_v, self.fuel

    def fuel_expense(self):
        """Calculates the cost of fuel based on engine type and fuel requirements."""
        if self.engine == SpaceX_Merlin:
            sum_ratio = 2.27 + 1
            part_of_fuel = self.fuel / sum_ratio

            LOX_fuel = part_of_fuel * 2.27
            RP_1_fuel = part_of_fuel

            LOX_fuel_price = LOX_fuel * 0.27
            RP_1_fuel_price = RP_1_fuel * 2.3

            total_fuel_price_in_dollars = round(
                LOX_fuel_price + RP_1_fuel_price)

            print(f"Total cost: {total_fuel_price_in_dollars}")

        elif self.engine == Spacex_Raptor:
            sum_ratio_raptor = 3.6 + 1
            part_of_fuel_raptor = self.fuel / sum_ratio_raptor

            LOX_fuel_raptor = part_of_fuel_raptor * 3.6
            CH4_fuel_raptor = part_of_fuel_raptor

            LOX_fuel_price_raptor = LOX_fuel_raptor * 0.27
            CH4_fuel_price_raptor = CH4_fuel_raptor * 8.8

            total_fuel_price_in_dollars_raptor = round(
                LOX_fuel_price_raptor + CH4_fuel_price_raptor)
            print(f"Total cost: {total_fuel_price_in_dollars_raptor}")

        elif self.engine == rs68:
            sum_ratio_rs68 = 5.97 + 1
            part_of_fuel_rs68 = self.fuel / sum_ratio_rs68

            LOX_fuel_rs68 = part_of_fuel_rs68 * 5.97
            LH2_fuel_rs68 = part_of_fuel_rs68

            LOX_fuel_price_rs68 = LOX_fuel_rs68 * 0.27
            LH2_fuel_price_rs68 = LH2_fuel_rs68 * 6.1

            total_fuel_price_in_dollars_rs68 = round(
                LOX_fuel_price_rs68 + LH2_fuel_price_rs68)
            print(f"Total cost: {total_fuel_price_in_dollars_rs68}")


# Engine instances with their specifications
SpaceX_Merlin = Engine(470, 3050, 342, 140, 981000)
Spacex_Raptor = Engine(1600, 3236, 350, 650, 2230000)
rs68 = Engine(6600, 4464, 412, 550, 3370000)

# Rocket instances with initial parameters
rocket_rapt = Rocket(10, 0, 4000, Spacex_Raptor, 0, 0) #https://forum.nasaspaceflight.com/index.php?topic=47506.1520, https://en.wikipedia.org/wiki/SpaceX_Raptor 
rocket_merl = Rocket(10, 0, 3900, SpaceX_Merlin, 0, 0) #https://en.wikipedia.org/wiki/SpaceX_Merlin, https://www.spacex.com/vehicles/falcon-9/
rocket_rs = Rocket(10, 0, 3900, rs68, 0, 0) #https://en.wikipedia.org/wiki/RS-68, https://www.slideshare.net/JackTaylor20/rs68 


def what_rocket_do_you_want():
    """Prompts the user to select a rocket engine and returns the corresponding rocket object."""
    print("Select an engine:\n1. SpaceX Merlin\n2. SpaceX Raptor\n3. RS-68")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        return rocket_merl
    elif choice == '2':
        return rocket_rapt
    elif choice == '3':
        return rocket_rs
    else:
        print("Invalid choice. Defaulting to SpaceX Merlin.")
        return rocket_merl


rocket = what_rocket_do_you_want()

rocket.calc_fuel_and_delta_v()
rocket.fuel_expense()
