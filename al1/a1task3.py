# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:58:24 2018

@author: QIDI
"""
## function 0
def fv_lump_sum(r, n, pv):
    """ return the future value of a lump sump pv invested at the periodic rate r for n periods
        input r, n, pv: any number (int or float)
    """
    return pv*(1+r)**n

# put your definitions for the remaining functions below


#function 2
def pv_lump_sum(r, n, fv):
    """ return the present value of a lump sum fv to be received in the future, discounted at the periodic rate r for n periods
        input r, n, pv: any number (int or float)
    """
    return fv/(1+r)**n


#function 3
def fv_annuity(r, n, pmt):
    """ return the future value of an annuity of pmt to be received each period for n periods, invested at the periodic rate r
        input r, n, pmt: any number (int or float)
    """
    return pmt*(((1+r)**n - 1)/r)



#function 4
def pv_annuity(r, n, pmt):
    """ return the present value of an annuity of pmt to be received each period for n periods, discounted at the rate r
        input r, n, pmt: any number (int or float)
    """
    return pmt*((1-(1+r)**-n)/r)


#function 5
def annuity_payment(r, n, pv):
    """ return the annuity payment for a present value of pv to be repaid at a periodic interest rate of r for n periods
        input r, n, pv: any number (int or float)
    """
    return (r*pv)/(1-(1+r)**-n)


if __name__ == '__main__':
    print('fv_lump_sum(0.08/12, 20*12, 400) returns:',fv_lump_sum(0.08/12, 20*12, 400))
    print('pv_lump_sum(0.06/2, 5*2, 500) return:',pv_lump_sum(0.06/2, 5*2, 500))
    print('fv_annuity(0.09/12, 10*12, 100) return',fv_annuity(0.09/12, 10*12, 100))
    print('pv_annuity(0.009/12, 60, 471.75) return',pv_annuity(0.009/12, 60, 471.75))
    print('annuity_payment(0.009/12, 60, 27667.44) return',annuity_payment(0.009/12, 60, 27667.44))
    