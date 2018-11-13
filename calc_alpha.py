from math import log

def f(u):
    return log((2.0 + u) / (1.0 + u),2)

def alpha(m):
    h = 0.0000001
    integral = 0
    for step in xrange(int(5/h)):
        integral += h * (f(step * h) ** m)
    return 1.0 / (m * integral)

for m in [16, 32, 64, 128]:
    print "alpha_"+str(m)+" = "+str(alpha(m))

"""
alpha_16 = 0.673101661564
alpha_32 = 0.697121856271
alpha_64 = 0.70920684336
alpha_128 = 0.715267915654
"""
