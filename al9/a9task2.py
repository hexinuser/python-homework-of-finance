# -*- coding: utf-8 -*-

from a9task1 import MCStockSimulator
import numpy as np
import math

class MCStockOption(MCStockSimulator):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockSimulator.__init__(self,s,t,r,sigma,nper_per_year)
        self.x = x
        self.num_trials = num_trials
    
    def __repr__(self):
        return 'MCStockOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)

    def value(self):
        print('Base class MCStockOption has no concrete implementation of .value()')
        return 0 
    
    def stderr(self):
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0
    
class MCEuroCallOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCEuroCallOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_last = self.generate_simulated_stock_values()[-1]
            values[i] = max(s_last-self.x,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value
    
#    def run_trails(self):
#        values = np.zeros(self.num_trials)
#        for i in range(self.num_trials):
#            s_last = self.generate_simulated_stock_values()[-1]
#            values[i] = max(s_last-self.x,0)*math.exp(-self.r*self.t)
#        self.mean = np.mean(values)
#        self.stdev = np.std(values)
class MCEuroPutOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCEuroPutOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_last = self.generate_simulated_stock_values()[-1]
            values[i] = max(self.x-s_last,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value

    
class MCAsianCallOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCAsianCallOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_mean = np.mean(self.generate_simulated_stock_values())
            values[i] = max(s_mean-self.x,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value

class MCAsianPutOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCAsianPutOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_mean = np.mean(self.generate_simulated_stock_values())
            values[i] = max(self.x-s_mean,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value

#aput = MCAsianPutOption(35, 30, 1.0, 0.08, 0.25, 100, 10000)
#print(aput.value())
#print(aput.stderr())

class MCLookbackCallOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCLookbackCallOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_max= np.max(self.generate_simulated_stock_values())
            values[i] = max(s_max-self.x,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value


class MCLookbackPutOption(MCStockOption):
    def __init__(self,s,x,t,r,sigma,nper_per_year,num_trials):
        MCStockOption.__init__(self,s,x,t,r,sigma,nper_per_year,num_trials)

    def __repr__(self):
        return 'MCLookbackPutOption s=%.2f, x=%.2f t=%.2f, r=%.2f, sigma=%.2f, nper_per_year=%d, num_trials=%d'%(self.s,
                                self.x,self.t,self.r,self.sigma,self.nper_per_year,self.num_trials)
    
    def value(self):
        values = np.zeros(self.num_trials)
        for i in range(self.num_trials):
            s_min = np.min(self.generate_simulated_stock_values())
            values[i] = max(self.x-s_min,0)*math.exp(-self.r*self.t)
        value = np.mean(values)
        self.stdev = np.std(values)
        return value









        