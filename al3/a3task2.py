# -*- coding: utf-8 -*-

def calc_returns(prices):
    """ return for periods 1 to n – there is no return for period 0
        input prices: any list (int)
    """
    n = len(prices)
    rate_price = []
    for i in range(1,n):
        rate_price.append(prices[i]/prices[i-1]-1)
    return rate_price

prices = [100,110,105,112,115]
returns = calc_returns(prices)
print(returns)
    
def process_stock_prices_csv(filename):
    """return a list of stock prices.
        input filename: any str
    """
    fr = open(filename,'r')
    price_list = []
    
    for line in fr.readlines()[1:]:
        value = line.strip().split(',')[-2]
        price_list.append(float(value))
    fr.close()
    return price_list

#def process_stock_prices_csv1(filename):
#    fr = open(filename,'r')
#    price_list = []
#    while True:
#        line = fr.readline()
#        if line == '':
#            break
#        else:
#            value = line.strip().split(',')[-2]
#            price_list.append(value)
#    return price_list
#
#filename = 'AAPL.csv'
#prices = process_stock_prices_csv(filename)
#    
 
from a3task1 import * 

filenames = ['AAPL.csv','BAC.csv', 'GOOG.csv', 'SPY.csv']  
def stock_report(filenames):
    """ return a string containing the entire report
        input filename: any str
    """
    list_price = []
    for filename in filenames:
        prices = process_stock_prices_csv(filename)
        rate_price = calc_returns(prices)
        list_price.append(rate_price)
    Symbol = 'Symbol:     '+'AAPL'+'      '+'BAC'+'       '+'GOOG'+'      '+ 'SPY'
    Mean = 'Mean:  '
    StDev = 'Stedv: '   
    Covar = 'Covar: '
    Correl = 'Correl:'  
    R_SQ = 'R_SQ:  '
    Beta = 'Beta:  '
    Alpha = 'Alpha: '
    for i in range(len(list_price)):
#        Mean.append(str(mean(list_price[i]))[:7])
#        StDev.append(str(stdev(list_price[i]))[:7]) 
#        Covar.append(str(covariance(list_price[i],list_price[-1]))[:7])
#        Correl.append(str(correlation(list_price[i],list_price[-1]))[:7])
#        R_SQ.append(str(rsq(list_price[i],list_price[-1]))[:7])
#        alpha,beta = simple_regression(list_price[i],list_price[-1])
#        Beta.append(str(beta)[:7])
#        Alpha.append(str(alpha)[:7])
        Mean += str('%10.5f' %mean(list_price[i]))
        StDev += str('%10.5f' %stdev(list_price[i]))
        Covar += str('%10.5f' %covariance(list_price[i],list_price[-1]))
        Correl += str('%10.5f' %correlation(list_price[i],list_price[-1]))
        R_SQ += str('%10.5f' %rsq(list_price[i],list_price[-1]))
        alpha,beta = simple_regression(list_price[i],list_price[-1])
        Beta += str('%10.5f' %beta)
        Alpha += str('%10.5f' %alpha)
        
    print_str =Symbol+'\n'+Mean+'\n'+StDev+'\n'+Covar+'\n'+Correl+'\n'+R_SQ+'\n'+Beta+'\n'+Alpha
    return print_str

#print(stock_report(filenames))
#





