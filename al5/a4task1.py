

def cashflow_times(n, m):
    """ develop the list of the times at which a bond makes coupon payments
        input n,m: any int
    """
    return [ i for i in range(1,n*m+1)]

#print(cashflow_times(3,4))
    
def discount_factors(r, n, m):
    """ return a list of discount factors for a given annualized interest rate r, for n years, and m discounting periods per year.
        input r: any float; n,m: any int
    """
    return [1/(1+r/m)**t for t in  range(1,n*m+1)]

#print(discount_factors(0.05, 5, 2))
    
def bond_cashflows(fv, c, n, m):
    """ return a list of cashflows for a bond specified by the parameters.
        input fv,r: any float; n,m: any int
    """
    time_list = cashflow_times(n, m)
    return [(int(t/(m*n))+c/m)*fv for t in time_list]

#print(bond_cashflows(1000, 0.08, 5, 2))

def bond_price(fv, c, n, m, r):
    """ return the price of a bond
        input fv, c, r: float; n,m:  int
    """
    time_list = cashflow_times(n, m)
    cashflows = bond_cashflows(fv, c, n, m)
    df = discount_factors(r, n, m)
    pv_list = [cashflows[t-1]*df[t-1] for t in time_list ]
    return sum(pv_list)

#print( bond_price(100, 0.04, 3, 2, 0.05) )

def bond_yield_to_maturity(fv, c, n, m, price):
    """ calculate the annualized yield_to_maturity on a bond
        input price fv, c: float; n,m:  int
    """
    r0 = 0
    r1 = 0.5
    price_after = bond_price(fv, c, n, m, r1)
    error_0 =  price_after-price
#    print('test_rate = %.8f, price = %.6f, diff = %.6f' %(r1,price_after,error_0))
    r2 = (r1+r0)/2
    while True:
        if abs(error_0)<=0.000001:
            return r2
        price_after = bond_price(fv, c, n, m, r2)
        error_1 =  price_after-price
#        print('test_rate = %.8f, price = %.6f, diff = %.6f' %(r2,price_after,error_1))
        if error_0*error_1 <0:
            r0 = r1  
        r1 = r2
        error_0 = error_1
        
        r2 = (r0+r1)/2
    
#print(bond_yield_to_maturity(1000, 0.08, 5, 1, 950))
        
######################################################################
### unit test code:
if __name__ == '__main__':
    times = cashflow_times(5,2)
    cashflows = bond_cashflows(100,0.04,5,2)
    df = discount_factors(0.02, 5, 2)
    price = bond_price(100, 0.04, 3, 2, 0.03)
    ytm = bond_yield_to_maturity(1000, 0.08, 5, 1, 950)

## end of unit test code
















