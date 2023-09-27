import math

engine_e_x  = 3050
mass = 3900

delta_V = int(input(""))

fuel = 2363734.1476801927
# Calculate delta-v
delta_V = engine_e_x * math.log((mass + fuel) / mass)

# Calculate fuel needed
print(fuel)
print(delta_V)
