h = 10000
v = 1000
G = 6.67430e-11  
M = 5.972e24     
R = 6400000      

def specific_energy():
    # om E = 0 så är det en helt rund omlopsbana, dä är hastigheten = roten ur (G * M) / (R + h)
    E = 0.5 * v**2 - (G * M) / (R + h)
    return(E)
def Eccentricitet():
    e = (1 + (2 * specific_energy())/(G * M))**0.5

# Halva Den Stora Axeln
def a():
    a = -(G*M)/(2 * specific_energy())
    return a

specific_energy()
