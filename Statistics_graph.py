
import math

class Statistics:
    
    def __init__(self, mean=0, sigma=1):
        self.mean  = mean
        self.sigma = sigma
        
    def Normal1D(self,x):
        return (1/(self.sigma*((2*math.pi)**0.5)))*math.exp(-(x-self.mean)**2/(2*self.sigma**2))
    
    def stat2(self,x):
        return 30*x
