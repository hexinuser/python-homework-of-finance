# -*- coding: utf-8 -*-

import math

def print_binomial_tree(tree):
    """ creates a nicely-formatted printout of the binomial tree
        input: tree: list[list]   
    """
    n = len(tree)
    for i in range(n):
        for j in range(n):
            if j<i:
                print('%8s' %' ',end='')
            else:
                print('%8.2f' %tree[i][j],end='')
        print()
#
#tree = [[0] * 5 for x in range(5)]
#print_binomial_tree(tree)            

def get_binomial_factors(sigma, rf, div, h):
    """ that calculates the factors needed to implement the binomial calculations
        input: sigma, rf, div, h: float
    """
    mu = math.exp((rf-div)*h+sigma*math.sqrt(h))
    d =  math.exp((rf-div)*h-sigma*math.sqrt(h))
    return (mu,d)

#print(get_binomial_factors(0.3, 0.06, 0.0, 0.025))
    
def get_risk_neutral_probability(sigma, rf, div, h):
    """ returns the risk-neutral probability associated with this option’s parameters. 
        input: sigma, rf, div, h: float
    """
    mu, d = get_binomial_factors(sigma, rf, div, h)
    p = (math.exp((rf-div)*h)-d)/(mu-d)
    return p

#print(get_risk_neutral_probability(0.3, 0.06, 0.0, 0.025))

def build_binomial_stock_price_tree(s, sigma, rf, div, T, n):
    """  returns binomial tree of simulated stock price movements
        input: S,sigma, rf, div, h, T: float; n:int
    """
    mu,d = get_binomial_factors(sigma, rf, div, T/n)
    tree = [[0]*(n+1) for x in range(n+1)]
    for i in range(n+1):
        for j in range(i,n+1):
            tree[i][j] = s*d**i*mu**(j-i)
    return tree

#t = build_binomial_stock_price_tree(100, 0.2, 0.04, 0.02, 1.0, 5)
#print_binomial_tree(t)

















    