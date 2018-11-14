# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:54:57 2018

@author: Evan_He
"""
from a1task3 import *
def life_cycle_model():
    risk_free_rate =float(input('Enter the current inflation-indexed risk-free rate of return: '))
    
#    risk_free_rate = input('Enter the current inflation-indexed risk-free rate of return: ')
#    risk_free_rate = float(risk_free_rate)
    
    age = int(input('Enter your age now: '))
    re_age= int(input('Enter your expected retirement age: '))
    annual_income = int(input('Enter your current annual income: '))

    work_year = re_age-age
    print('You have %.5f remaining working years with an income of $%d per year.' %(work_year,annual_income))

    print('You have '+str(work_year)+' remaining working years with an income of $'+str(annual_income)+' per year.')

    human_capital= pv_annuity(risk_free_rate, work_year, annual_income)
    print('The present value of your human capital is about $'+str(int(human_capital)))
    
    assets = int(input('Enter the value of your financial assets: '))

    eco_worth = human_capital+assets
    print('Your economic net worth is: '+str(int(eco_worth)))

    living_standard = annuity_payment(risk_free_rate,100-age,eco_worth)

    print('Your sustainable standard of living is about $'+str(int(living_standard))+' per year')
    save_money = annual_income - living_standard
    print('To achieve this standard of living to age 100, you must save $'+str(int(save_money))+' per year.')
    
#if __name__ == '__main__':
#    life_cycle_model()
    

work = '22'
ann ='sadf'
print('You have %s remaining working years with an income of $%s per year.' %(work,ann))










