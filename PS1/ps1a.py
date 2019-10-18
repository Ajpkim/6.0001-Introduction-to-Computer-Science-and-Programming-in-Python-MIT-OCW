# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:36:55 2019

@author: alexk
"""

total_cost = float(input('Enter the cost of your dream home: '))
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))


portion_down_payment = 0.25*(total_cost)
current_savings = 0.0
r = 0.04
months_before_purchase = 0

while current_savings < portion_down_payment:
    current_savings += current_savings*(r/12.0) + portion_saved*(annual_salary/12.0)
    months_before_purchase += 1
    
print ('You have to save for', months_before_purchase, 'months.')
