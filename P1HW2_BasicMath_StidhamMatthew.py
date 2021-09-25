# In this project you'll see how a cable bill is used to create monthly and annual charges
# 09/25//2021
# CTI-110 P1HW2 - Basic Math
# Matthew Stidham

expense = input() # creation of word input for expense

charge = int(input()) #creation of numerical input for charge

print('Enter name of expense:', expense) # labeling expense input

print('Enter monthly charge:', charge) # labeling charge input

print('Bill:', expense,'---------- ','Before Tax: ', "$%.2f" % charge) # output of expense and charge with a rounded total 

month_tax = charge * 0.06 # monthly tax is 6%

print('Monthly Tax:    ', "$%.2f" % month_tax) # output of monthly tax rounded to the second decimal place

month_total = charge + month_tax # month total adds tax to the original charge

print('Monthly Charge: ', "$%.2f" % month_total) # output of monthly ttotal rounded to the second decimal place

annual_total = month_total * 12.0 # annual total multiplies the month total by 12 months

print('Annual Charge:  ', "$%.2f" % annual_total) # output of annual total rounded to the second decimal place

