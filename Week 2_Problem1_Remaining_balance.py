#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:46:13 2019

@author: aydinj
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04 # Minimum monthly payment rate
monthlyInterestRate = annualInterestRate/12.0
minimumMonthlyPayment = monthlyPaymentRate * balance
monthlyUnpaidBalance = balance - minimumMonthlyPayment
for i in range(1, 13):
    updatedBalanceEachMonth = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    minimumMonthlyPayment = monthlyPaymentRate * updatedBalanceEachMonth
    monthlyUnpaidBalance = updatedBalanceEachMonth - minimumMonthlyPayment
    print(f'Month {i} Remaining balance: {round(updatedBalanceEachMonth, 2)}')
        
print(f'Remaining balance: {round(updatedBalanceEachMonth, 2)}')