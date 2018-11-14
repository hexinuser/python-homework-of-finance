# -*- coding: utf-8 -*-


from a6task1 import *

import math
def build_euro_call_value_tree(s, x, sigma, rf, div, T, n):
    """ return returns a binomial option value tree for European-style call options
        input: S, x, sigma, rf, div, T: float; n:int
    """
    tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    x = [x]*(n+1)
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
    for j in range(n,-1,-1):
        for i in range(j+1):
            if j ==n: 
                tree[i][j] = max(tree[i][j]-x[i],0)
            else:
                tree[i][j] = math.exp(-(rf-div)*T/n)*(p*tree[i][j+1]+(1-p)*tree[i+1][j+1])
    return tree

#t = build_euro_call_value_tree(25, 22, 0.25, 0.05, 0.03, 0.25, 5)
#print_binomial_tree(t)

def euro_call_value(s, x, sigma, rf, div, T, n):
    """ return value should be the value in dollars today
        input: S, x, sigma, rf, div, T: float; n:int
    """
    tree = build_euro_call_value_tree(s, x, sigma, rf, div, T, n)
    return tree[0][0]


#print(euro_call_value(25, 22, 0.20, 0.05, 0.03, 0.25, 5))
#print(euro_call_value(25, 22, 0.20, 0.05, 0.03, 0.25, 100))
    
def build_euro_put_value_tree(s, x, sigma, rf, div, T, n):
    """ returns a binomial option value tree for European-style put options
        input: S, x, sigma, rf, div, T: float; n:int
    """
    tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    x = [x]*(n+1)
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
    for j in range(n,-1,-1):
        for i in range(j+1):
            if j ==n: 
                tree[i][j] = max(x[i]-tree[i][j],0)
            else:
                tree[i][j] = math.exp(-(rf-div)*T/n)*(p*tree[i][j+1]+(1-p)*tree[i+1][j+1])
    return tree
#t = build_euro_put_value_tree(20, 22, 0.25, 0.05, 0.03, 0.25, 5)
#print_binomial_tree(t)
#t = build_euro_put_value_tree(90, 100, 0.3, 0.06, 0.02, 0.25, 10)
#print_binomial_tree(t)
    
def euro_put_value(s, x, sigma, rf, div, T, n):
    """ return value should be the value in dollars today
        input: S, x, sigma, rf, div, T: float; n:int
    """
    tree = build_euro_put_value_tree(s, x, sigma, rf, div, T, n)
    return tree[0][0]

#print(euro_put_value(25, 30, 0.30, 0.05, 0.03, 0.5, 10))


def build_amer_put_value_tree(s, x, sigma, rf, div, T, n):
    """ returns a binomial option value tree for American-style put options.
        input: S, x, sigma, rf, div, T: float; n:int
    """
    tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    tree1 = tree[:][:]
    x = [x]*(n+1)
    p = get_risk_neutral_probability(sigma, rf, div, T/n)
#    p0 = 
    for j in range(n,-1,-1):
        for i in range(j+1):
            if j ==n:    
                tree[i][j] = max(x[i]-tree[i][j],0)
            else:
                tree[i][j] = max(math.exp(-(rf-div)*T/n)*(p*tree[i][j+1]+(1-p)*tree[i+1][j+1]),x[i]-tree1[i][j])
#                tree[i][j] = math.exp(-(rf-div)*T/n)*(p*tree[i][j+1]+(1-p)*tree[i+1][j+1])
    return tree


#t = build_euro_put_value_tree(100, 100, 0.3, 0.06, 0.04, 1.0, 10)
#print_binomial_tree(t)


def amer_put_value(s, x, sigma, rf, div, T, n):
    tree = build_amer_put_value_tree(s, x, sigma, rf, div, T, n)
    return tree[0][0]

#print(euro_put_value(25, 30, 0.10, 0.05, 0.03, 0.5, 10))
#
#print(amer_put_value(25, 30, 0.30, 0.05, 0.03, 0.5, 100))



















