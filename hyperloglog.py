from hashlib import sha1
from math import pow
from numpy.random import randint

class HyperLogLog:
    def __init__(self, b):
        if b not in [4, 5, 6, 7]:
            raise ValueError("b must be in range [4 .. 7]")
        
        self.b = b
        self.m = 1 << self.b
        self.alpha = self.__get_alpha(self.m)
        self.M = [0]*self.m        
    
    
    def __get_alpha(self, m):
        if m == 16:
            return 0.6731
        elif m == 32:
            return 0.6971
        elif m == 64:
            return 0.7092
        elif m == 128:
            return 0.7153
        else:
            raise ValueError("m must be in [16, 32, 64, 128]")
    
    
    def __rho(self, w):
        if w == 0:
            return 32 - self.b + 1
        else:
            return bin(w)[::-1].find('1') + 1
    
    
    def add(self, v):
        x = int(sha1(str(v)).hexdigest()[:8], 16)
        j = x & (self.m - 1)
        w = x >> self.b
        self.M[j] = max(self.M[j], self.__rho(w))
    
    def count(self):
        return self.alpha * float(self.m ** 2) / sum(pow(2.0, -e) for e in self.M)


if __name__ == "__main__":
    s = set()
    h = HyperLogLog(7)
    for i in xrange(1000000):
        r = randint(1000)*randint(1000)+randint(1000)
        h.add(r)
        s.add(r)
        if i % 10000 == 9999:
            act = len(s)
            est = h.count()
            print "round: "+str(i)+", act: "+str(act)+", est: "+str(est)+", act/est: "+str(act/est)
