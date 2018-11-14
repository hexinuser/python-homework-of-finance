# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt

class MCStockSimulator:
    """his class will serve as a base class for option pricing classes"""
    def __init__(self,s,t,r,sigma,nper_per_year):
        self.s = s
        self.t = t
        self.r = r
        self.sigma = sigma
        self.nper_per_year = nper_per_year 
    
    def __repr__(self):
        return 'StockSimulator s=$%.2f, t=%.2f (years), r=%.2f, sigma=%.2f, nper_per_year=%d'%(self.s,
                                self.t,self.r,self.sigma,self.nper_per_year)

    def generate_simulated_stock_returns(self):
        dt = 1/self.nper_per_year
        n = int(self.t*self.nper_per_year)
        stock = np.zeros(n)
        for i in range(n):
            z = np.random.normal()
            stock[i] = (self.r-self.sigma**2/2)*dt+z*self.sigma*math.sqrt(dt)
        return stock
    
    def generate_simulated_stock_values(self):
        stock = self.generate_simulated_stock_returns()
        n = int(self.t*self.nper_per_year)
        values = self.s*np.ones(n+1)
        for i in  range(n):
            values[i+1] = values[i]*math.exp(stock[i])
        return values
    
    def plot_simulated_stock_values(self, num_trials = 1):
        n = int(self.t*self.nper_per_year)
        years = np.linspace(0,self.t,n+1)
#        years = np.arange(0,self.t+dt,dt)
        for i in range(num_trials):
            values = self.generate_simulated_stock_values()
            plt.plot(years,values)
#            plt.show()
        plt.xlabel('years')
        plt.ylabel('$ values')
        plt.title(str(num_trials)+' simulated trials')
