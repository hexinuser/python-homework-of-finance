# -*- coding: utf-8 -*-


from a8task1 import *

def generate_option_value_table(s, x, t, sigma, rf, div):
    """ generate a printout to illustrate the change in option prices with 
        respect to the change in the underlying stock price. 
        input: s,x,t,sigma,rf,div: float
    """
    call = BSEuroCallOption(s,x,t,sigma,rf,div)
    put = BSEuroPutOption(s,x,t,sigma,rf,div)
    print(call)
    print(put)
    print()
    print('Change in option values w.r.t. change in stock price:')
    print('     price \t call value \t put value \t call delta \t put delta')
    for i in range(21):
        call.s = s -10 + i
        put.s = s -10 + i
        print('$ %8.2f \t $ %8.2f \t $ %8.2f \t  %8.4f \t  %8.4f'%(call.s,call.value(),put.value(),call.delta(),put.delta()))
        
#generate_option_value_table(100,100,0.5,0.25,0.04,0.02)
        
def calculate_implied_volatility(option, value):
    """ calculate the implied volatility of an observed option
        input: option: class, value:float
    """
    if option.value() > value:
        r1 = 0
        r2 = option.sigma
    else:
        r1 = option.sigma
        r2 = 1
    error = abs(option.value() - value)
    while error > 1e-3:
        print('sigma=%.6f, value=%.6f'%(option.sigma,option.value()))
        option.sigma = (r1+r2)/2
        if option.value() > value:
            r2 = option.sigma
        else:
            r1 = option.sigma
        error = abs(option.value() - value)
    return option.sigma
#call = BSEuroCallOption(56.33, 60, 100/365, 0.5, 0.02, .02)
#print(calculate_implied_volatility(call, 0.79))
#put = BSEuroPutOption(56.33, 55, 100/365, 0.5, 0.02, 0.02)
#print(calculate_implied_volatility(put, 1.57))

            
            
            
    