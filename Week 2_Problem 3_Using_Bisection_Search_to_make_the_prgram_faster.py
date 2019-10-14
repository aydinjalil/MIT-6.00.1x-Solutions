#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:55:59 2019

@author: aydinj
"""

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12.0
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
minimumFixedMonthlyPayment = (lowerBound + upperBound)/2
monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
    #updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance 
epsilon = 0.01
while True:
    for i in range(12):
        updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        monthlyUnpaidBalance = updatedBalanceEachMonth - minimumFixedMonthlyPayment
         #print(updatedBalanceEachMonth, minimumFixedMonthlyPayment)
    if (updatedBalanceEachMonth + epsilon) < 0:
        upperBound = minimumFixedMonthlyPayment
        minimumFixedMonthlyPayment = (lowerBound + upperBound)/2
    elif (updatedBalanceEachMonth - epsilon) > 0:
        lowerBound = minimumFixedMonthlyPayment
        minimumFixedMonthlyPayment = (lowerBound + upperBound)/2
    else:
        break
            
    monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment  
print(round(minimumFixedMonthlyPayment, 2))
            