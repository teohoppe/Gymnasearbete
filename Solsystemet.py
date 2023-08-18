import math
from math_pi import pi


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


# Time to revolve around earth 2 358 720 Sekonds
# 384 400 000 meters to the moon
moon = Planet(7.35 * 10**24, 1737.4 * 1000, 1.62, 1022)
earth = Planet(5.972 * 10**24, 6371 * 1000, 9.82, 0)

tick_speed =  2360800 
time = 0

def moon_orbit(tick_speed, moon, earth):
        distance = tick_speed * moon.speed
        v = (distance * 360) / (math.pi * 2 * 384400000)
        print(v)

def main():
    time += tick_speed
    
moon_orbit(tick_speed, moon, earth)