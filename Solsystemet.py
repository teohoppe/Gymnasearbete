import math
from math import pi
import time
import random


class Planet:
    def __init__(self, mass, radius, g, speed):
        self.mass = mass
        self.radius = radius
        self.g = g
        self.speed = speed


class Rocket:
    def __init__(self, distands_from_earth, speed, fuel, mass):
        self.distands_from_earth = distands_from_earth
        self.speed = speed
        self.fuel = fuel
        self.mass = mass


# Time to revolve around earth 2358720 Sekonds
# 384400000 meters to the moon
moon = Planet(7.35 * 10**24, 1737.4 * 1000, 1.62, 1022)
earth = Planet(5.972 * 10**24, 6371 * 1000, 9.82, 0)

# Hur snabbt simuleringen körs(nogranhet)
tick_speed = 100


def moon_orbit(tick_speed, moon, earth):    
    
    v = 0
    time_from_start = 0
    while True:

        # Uträkning som använder månens hastighet och avstånd till jorden för att avgöra vart månen är
        time_from_start += 1
        distance = tick_speed * moon.speed
        v += (distance * 360) / (math.pi * 2 * 384400000)

        # hittar mån kordinater
        find_moon_x_and_y(v, time_from_start)

        # Avgör när månen har åkt ett helt varv
        if v > 360:
            print(v)
            v = 0
            print('MÅNAD')
            print(time_from_start)
            break


def find_moon_x_and_y(v, time_from_start):
    # Sinusats för att hitta x och y kordinater till månen
    #orbit = ((x^(2))/(384400^(2)))+((y^(2))/(383800^(2)))
    # Alex säger att det går bra annars att använda sig av att orbit är en perfekt cirkel istället för en elips med 0.16% skillnad

    #G
    v_in_rad = math.radians(v)
    moon_y = math.sin(v_in_rad) * 384400000
    moon_x = math.cos(v_in_rad) * 384400000

    print(round(moon_y, 0))


def main():
    time += tick_speed



moon_orbit(tick_speed, moon, earth)
