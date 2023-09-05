import math
from math import pi
import time
import random


class Planet:
    def __init__(self, mass, radius, g, speed, distanse_from_earth):
        self.mass = mass
        self.radius = radius
        self.g = g
        self.speed = speed
        self.distanse_from_earth = distanse_from_earth


class Rocket:
    def __init__(self, distands_from_earth, speed, fuel, mass, thrust):
        self.distands_from_earth = distands_from_earth
        self.speed = speed
        self.fuel = fuel
        self.mass = mass
        self.thrust = thrust

    def fuel_mass(self):
        fuel_mass = 1
        return self.fuel * fuel_mass

        # d_from_e  speed fuel  M     thrust
rocket = Rocket(160000, 160, 50, 100, 10000)

# Time to revolve around earth 2358720 Sekonds
# 384400000 meters to the moon
moon = Planet(7.35 * 10**24, 1737.4 * 1000, 1.62, 1022, 384400000)
earth = Planet(5.972 * 10**24, 6371 * 1000, 9.82, 0, 0)

# Hur snabbt simuleringen körs(nogranhet)
tick_speed = 100


def moon_orbit(tick_speed, moon, earth):
    angel = 0
    time_from_start = 0
    while True:

        # Uträkning som använder månens hastighet och avstånd till jorden för att avgöra vart månen är
        time_from_start += 1
        distance = tick_speed * moon.speed
        angel += (distance * 360) / (math.pi * 2 * 384400000)

        # hittar mån kordinater
        find_moon_x_and_y(angel, time_from_start)

        # Avgör när månen har åkt ett helt varv
        if angel > 360:
            print(angel)
            angel = 0
            print('MÅNAD')
            print(time_from_start)
            break


def rocket_orbit(tick_speed, rocket):
    # calk delta V
    delta_V = rocket.thrust * \
        math.log((rocket.mass + rocket.fuel_mass()) / (rocket.mass))
    print(delta_V)


def pull_from_earth_and_moon(rocket, moon):
    G = 6.674 * 10**-11
    # Gravity pull from earth and moon
    f_moon = G * ((rocket.mass * moon.mass) /
                  (moon.distanse_from_earth - rocket.distands_from_earth)**2)
    f_earth = G * ((rocket.mass * earth.mass) /
                   (rocket.distands_from_earth)**2)
    print(f_earth)
    print(f_moon)

    # Total force on rocket
    if f_moon < f_earth:
        f = f_moon - f_earth
    else:
        f = f_earth - f_moon

    print(f)


def find_moon_x_and_y(angel, time_from_start):
    # Sinusats för att hitta x och y kordinater till månen
    # orbit = ((x^(2))/(384400^(2)))+((y^(2))/(383800^(2)))
    # Alex säger att det går bra annars att använda sig av att orbit är en perfekt cirkel istället för en elips med 0.16% skillnad

    v_in_rad = math.radians(angel)
    moon_y = math.sin(v_in_rad) * 384400000
    moon_x = math.cos(v_in_rad) * 384400000


def calc_speed_in_orbit(moon, rocket, earth):
    # v**2 = µ((2/r) - (1/a))
    pass


def main():
    while True:
        menu = int(input("Press (1) to make rocket"))
        if menu == 1:
            # diseinga raket
            pass

    pass


pull_from_earth_and_moon(rocket, moon)
