# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


##### Given's for problem... (more generalizable program is below)
# semi-annual raise is 7%
# investments have return of 4% annually
# down payment is 25% of total home cost
# total cost of dream home is 1m
# AK: Problem is to use bisection search to solve for savings rate given an annual 
# salary for which current savings after 36 months is within 100 of down payment cost 


#for months in range(36):
#    current_savings += current_savings*(r/12)+(annual_salary/12)
#        if months % 6 == 0:
#            annual_salary += annual_salary * semi_annual_raise
#if abs(current_savings - portion_down_payment) > 100:
#    print ('It is not possible to pay the down payment in 3 years')



starting_salary = float(input('Enter starting annual salary: '))
annual_salary = starting_salary
total_cost = 1000000
portion_down_payment = .25*total_cost
semi_annual_raise = 0.07
r = 0.04
current_savings = 0
steps = 0

low = 0
high = 10000
savings_rate = (high + low)/2

while abs(current_savings - portion_down_payment) >= 100: 
    
    
    for months in range(36):
        current_savings += current_savings*(r/12)+(savings_rate/10000)*(annual_salary/12)
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    steps += 1
    
# These prints are just to help troubleshoot...
#    print ('Savings rate: ', savings_rate/10000)
#    print ('Current savings: ', current_savings) 
#    print ('Steps: ', steps)
    
    if abs(current_savings - portion_down_payment) > 100: #If while loop not satisfied
        
        if current_savings - portion_down_payment > 100: #Reducing search area by half
            high = savings_rate
        else:
            low = savings_rate    
        savings_rate = (high + low)/2 # Resetting savings_rate (guess)
        current_savings = 0
        months = 0
        annual_salary = starting_salary
    
    if steps > 1000:   # Not ideal solution to addressing impossible cases
        break
        
   
if steps > 1000:
    print ('There is no possible savings rate')
else:
        
    print ('Best savings rate is: ', savings_rate/10000)
    print ('Steps in bisection search: ', steps)

###############
# Version with all user inputs:

#starting_salary = float(input('Enter starting annual salary: '))
#total_cost = float(input('Enter the cost of your dream home: '))
#portion_down_payment = float(input('Enter down payment %, as a decimal: ')) * total_cost
#semi_annual_raise = float(input('Enter expected semi-annual raise, as a decimal: '))
#r = float(input('Enter expected annual investment return on savings: '))
#annual_salary = starting_salary
#current_savings = 0
#steps = 0
#
#
#low = 0
#high = 10000
#savings_rate = (high + low)/2
#
#while abs(current_savings - portion_down_payment) >= 100:
#    for months in range(1,37):
#        current_savings += current_savings*(r/12)+(savings_rate/10000)*(annual_salary/12)
#        if months % 6 == 0:
#            annual_salary += annual_salary * semi_annual_raise
#    steps += 1
#        
## These prints are just to help troubleshoot...
##    print ('Savings rate: ', savings_rate/10000)
##    print ('Current savings: ', current_savings) 
##    print ('Steps: ', steps)
#    
#    if abs(current_savings - portion_down_payment) >= 100:
#        
#        if current_savings - portion_down_payment > 100:
#            high = savings_rate
#        else:
#            low = savings_rate
#            
#        savings_rate = (high + low)/2
#        current_savings = 0
#        months = 0
#        annual_salary = starting_salary
#    
#    
#print ('Best savings rate is: ', savings_rate/10000)
#print ('Steps in bisection search: ', steps)

















