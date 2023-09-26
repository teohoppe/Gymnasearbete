engine_thrust = 3050
mass = 3900
fuel = 93
import math


delta_V = engine_thrust * math.log((mass + fuel) / mass)
print(delta_V)
