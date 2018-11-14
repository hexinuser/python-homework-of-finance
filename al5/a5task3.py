# -*- coding: utf-8 -*-

from a4task1 import cashflow_times,discount_factors, bond_cashflows
from a5task1 import *
from a5task2 import *


def bond_price(fv, c, n, m, r):
    """ return the price of a bond
        input fv, c, r: float; n,m:  int
    """

    cashflows = [bond_cashflows(fv, c, n, m)]
    df =[discount_factors(r, n, m)]
    
    return dot_product(cashflows,transpose(df))[0][0]

#print(bond_price(1000, 0.00, 5, 2, 0.09))
    
def bootstrap(cashflows, prices):
    """ find the implied prices of zero-coupon bonds 
        input: cashflows,prices: list
    """
    cf_inv = inverse_matrix(cashflows)
    return dot_product(cf_inv,prices)

#CF = [[105,0,0],[6,106,0],[7,7,107]]
#P = [[99.5], [101.25], [100.35]]
#D = bootstrap(CF, P)
#print_matrix(D, 'Implied Discount Factors')