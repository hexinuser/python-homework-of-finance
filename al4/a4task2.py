

from a4task1 import *

def bond_duration(fv, c, n, m, r):
    """ return the duration metric for a bond
        input fv,c,r: float; m,n: int
    """
    time_list = cashflow_times(n, m)
    cashflows = bond_cashflows(fv, c, n, m)
    df = discount_factors(r, n, m)
    pv_list = [t*cashflows[t-1]*df[t-1] for t in time_list ]
    
    price_bound = bond_price(fv, c, n, m, r)
    
    return sum(pv_list)/price_bound/m

print(bond_duration(1000, 0.14, 5, 2, 0.07))
    
def bond_convexity(fv, c, n, m, r):
    """return the convexity metric for a bond
    input fv,c,r: float; m,n: int
    """
    time_list = cashflow_times(n, m)
    cashflows = bond_cashflows(fv, c, n, m)
    df = discount_factors(r, n, m)
    
    price_bound = bond_price(fv, c, n, m, r)
    pv_list = [(t+1)*t*cashflows[t-1]*df[t-1] for t in time_list ]
    return sum(pv_list)/(1+r/m)**2/(price_bound*m)/m

#print(bond_duration(1000,0.061, 6,2, 0.10))
    
def estimate_change_in_price(fv, c, n, m, r):
    """ we will estimate the change in a bond’s price in response to change in the interest rate.
        input fv,c,r:float; n,m: int
    """
    rate_list = [i/1000 for i in range(int(r*1000)-10,int(r*1000)+10+1)]
    price_r = bond_price(fv, c, n, m, r)
    print(' rate        price            dp         pctchg        e_pctchgD       e_pctchgDC')
    for ri in rate_list:
        price = bond_price(fv, c, n, m, ri)
        dp = price-price_r
        pctchg = dp/price_r
        e_pct_1 = -bond_duration(fv, c, n, m, r)/(1+r/m)*(ri-r)
        e_pct_2 = e_pct_1 + bond_convexity(fv, c, n, m, r)/2*(ri-r)**2
        print( '%5.4f   $ %8.2f      $ %6.2f       %6.3f%%        %6.3f%%         %6.3f%%'%(ri,price,dp,pctchg*100,e_pct_1*100,e_pct_2*100))

estimate_change_in_price(1000.00, 0.1,4, 2, 0.06)











        