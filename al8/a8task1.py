# -*- coding: utf-8 -*-
from scipy.stats import norm
import math

class BSOption:
    """Write a definition for the base class BSOption"""
    def __init__(self,s,x,t,sigma,rf,div):
            self.s = s 
            self.x = x
            self.t = t
            self.sigma = sigma
            self.rf = rf
            self.div = div
            
    def __repr__(self):
        return 's = $%.2f, x = $%.2f, t =%.2f (years), sigma = %.3f, rf = %.3f, div = %.2f'%(self.s,self.x,
                                              self.t,self.sigma,self.rf,self.div)
    
    def d1(self):
        return 1/(self.sigma*math.sqrt(self.t))*(math.log(self.s/self.x)+(self.rf-self.div
                  +self.sigma**2/2)*self.t)
    
    def d2(self):
        return self.d1()-self.sigma*math.sqrt(self.t)
    
    def nd1(self):
        return norm.cdf(self.d1())
    
    def nd2(self):
        return norm.cdf(self.d2())
    
    def value(self):
        print('Cannot calculate value for base class BSOption.')
        return 0
    
    def delta(self):
        print('annot calculate delta for base class BSOption.')
        return 0 

class BSEuroCallOption(BSOption):
    """Write a definition for the class BSEuroCallOption, which 
      inherits from the base class BSOPtion and implements the pricing
      algorithm for a European-style call option
      """
    def __init__(self,s,x,t,sigma,rf,div):
        BSOption.__init__(self,s,x,t,sigma,rf,div)
        
    def __repr__(self):
        result = 'BSEuroCallOption, value = $%.2f,\n' %self.value()
        result +='parameters = (s = $%.2f, x = $%.2f, t =%.2f (years), sigma = %.3f, rf = %.3f, div = %.2f)'%(self.s,self.x,
                                              self.t,self.sigma,self.rf,self.div)
        return result
    
    def value(self):
        return self.nd1()*self.s*math.exp(-self.div*self.t)-self.nd2()*self.x*math.exp(-self.rf*self.t)
    
    def delta(self):
        return self.nd1()

#call = BSEuroCallOption(100, 90, 1.0, 0.30, 0.06, 0.00)
#print(call.value()) 
#call = BSEuroCallOption(100, 100, 1, 0.30, 0.06, 0.00)   
#print(call)
#    
class BSEuroPutOption(BSOption):
    """ Write a definition for the class BSEuroPutOption, which inherits
     from the base class BSOPtion and implements the pricing algorithm
     for a European-style put option. 
    """
    def __init__(self,s,x,t,sigma,rf,div):
        BSOption.__init__(self,s,x,t,sigma,rf,div)
        
    def __repr__(self):
        result = 'BSEuroPutOption, value = $%.2f,\n' %self.value()
        result +='parameters = (s = $%.2f, x = $%.2f, t =%.2f (years), sigma = %.3f, rf = %.3f, div = %.2f)'%(self.s,self.x,
                                              self.t,self.sigma,self.rf,self.div)
        return result
    
    def value(self):
        return (1-self.nd2())*self.x*math.exp(-self.rf*self.t)-(1-self.nd1())*self.s*math.exp(-self.div*self.t)
    
    def delta(self):
        return self.nd1()-1
    
#call = BSEuroCallOption(100, 100, 0.5, 0.25, 0.04, 0.02)
#print(call.delta())
#put = BSEuroPutOption(100, 100, 0.5, 0.25, 0.04, 0.02)
#print(put.delta())
#    
    

    
    
    
    
    