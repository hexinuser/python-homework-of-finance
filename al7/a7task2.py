# -*- coding: utf-8 -*-

from a7task1 import *


class BondPortfolio:
    """creating a class definition for class BondPortfolio"""
    def __init__(self):
        self.__data = []
    
    def __repr__(self):
        print_out = 'BondPortfolio contains %d bonds:\n' %(len(self.__data))
        for bond in self.__data:
            print_out += bond.__repr__()+'\n'
        print_out += 'Portfolio value: \t\t $%.2f\n' %self.get_value()
        print_out += 'Portfolio yield to maturity: \t %.4f%%\n' %(self.get_yield_to_maturity()*100)
        print_out += 'Portfolio duration: \t\t %.2f\n' %self.get_duration()
        print_out += 'Portfolio convexity: \t\t %.2f\n' %self.get_convexity()
        return print_out
    
    def add_bond(self, b):
        if type(b) ==Bond:
            self.__data.append(b)
    
    def get_value(self):
        values = [bond.get_price() for bond in self.__data]
        return sum(values)
    
    def get_yield_to_maturity(self):
         values = [bond.get_price() for bond in self.__data]
         ytm = [bond.get_yield_to_maturity()*bond.get_price() for bond in self.__data]
         return sum(ytm)/sum(values)
     
    def get_duration(self):
         values = [bond.get_price() for bond in self.__data]
         dur = [bond.get_duration()*bond.get_price() for bond in self.__data]
         return sum(dur)/sum(values)        
    
    def get_convexity(self):
         values = [bond.get_price() for bond in self.__data]
         con = [bond.get_convexity()*bond.get_price() for bond in self.__data]
         return sum(con)/sum(values)    
     
    def shift_ytm(self, delta_ytm):
        for bond in self.__data:
            new_ytm = bond.get_yield_to_maturity()+delta_ytm
            bond.set_yield_to_maturity(new_ytm)

#bp = BondPortfolio()   
#b1 = Bond(10000, 2, .06)
#b1.set_yield_to_maturity(0.07)
#bp.add_bond(b1)
#print(bp)
#b2 = Bond(10000, 5, .08)
#b2.set_yield_to_maturity(0.09)
#bp.add_bond(b2)
#print(bp)


#bp = BondPortfolio()
#b1 = Bond(10000, 2, .06)
#b1.set_yield_to_maturity(0.07)
#bp.add_bond(b1)
#b2 = Bond(10000, 5, .08)
#b2.set_yield_to_maturity(0.09)
#bp.add_bond(b2)
#b3 = Bond(5000, 10) # 10-year zero-coupon bond
#b3.set_yield_to_maturity(0.10)
#bp.add_bond(b3)
#print(bp)
#print(bp.get_value())
#print(bp.get_yield_to_maturity())
#print(bp.get_duration())
#print(bp.get_convexity())

#bp.shift_ytm(0.01) # a 1% increase in interest rates
#print(bp)
#bp.shift_ytm(-0.005) # a 0.5% decrease in interest rates
#print(bp)


   