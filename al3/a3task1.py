# -*- coding: utf-8 -*-


def mean(values):
    """ return the mean of those values
        input values: any list (int)
    """
    n = len(values)
    sum_val = 0
    for i in range(n):
        sum_val += values[i]
    return sum_val/n

#x = [4,4,3,6,7]
#print( mean(x))
    
def variance(values):
    """ return the population variance of the values in that list
        input values: any list (int)
    """
    n = len(values)
    mean_u = mean(values)
    sum_val = 0
    for i in range(n):
        sum_val += (values[i]-mean_u)**2
    return sum_val/n

#x = [4,4,3,6,7]
#print(variance(x))

def stdev(values):
    """ return the population standard deviation of the values
        input values: any list (int)
    """
    return variance(values)**(0.5)
#x = [4,4,3,6,7]
#print(stdev(x))


def covariance(x,y):
    """ return the population covariance for those two lists
        input x,y: any list (int)
    """
    assert(len(x) == len(y))
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    sum_val = 0
    for i in range(n):
        sum_val += (x[i]-mean_x)*(y[i]-mean_y)
    return sum_val/n

#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(covariance(x,y))

def correlation(x,y) :
    """ return the coefficient between these data series
        input x,y: any list (int)
    """
    assert(len(x) == len(y))
    sigma_xy = covariance(x,y)
    sigma_x = stdev(x)
    sigma_y = stdev(y)
    return sigma_xy/(sigma_x*sigma_y)
#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(correlation(x,y))

def rsq(x,y):
    """ return the square of the correlation between those two data series
        input x,y: any list (int)
    """
    assert(len(x) == len(y))
    return correlation(x,y)**2

#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(rsq(x,y))


def simple_regression(x,y):
    """ return the regression coefficients between these data series
        input x,y: any list (int)
    """
    assert(len(x) == len(y))
    beta = covariance(x,y)/variance(x)
    alpha = mean(y)-beta*mean(x)
    return alpha, beta

#x = [4,4,3,6,7]
#y = [6,7,5,10,12]
#print(simple_regression(x,y))






































