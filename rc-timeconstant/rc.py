import math

R = 1e3
C = 1e-12

tau = R*C

f = 1/(2*math.pi * tau)

print "%1.2g" % f
