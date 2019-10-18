# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:59:01 2019

@author: alexk
"""

total_cost = float(input('Enter the cost of your dream home: '))
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
semi_annual_raise = float(input('Enter your expected semi-annual rase, as a decimal: '))

portion_down_payment = 0.25*(total_cost)
current_savings = 0.0
r = 0.04
months_before_purchase = 0


while current_savings < portion_down_payment:
    current_savings += current_savings*(r/12.0) + portion_saved*(annual_salary/12.0)
    months_before_purchase += 1
    if months_before_purchase % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
    
print ('You have to save for', months_before_purchase, 'months.')
