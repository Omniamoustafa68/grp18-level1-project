import math

print('--- program to calculate this loan formula ---')
# input = loanAmount | monthlyInterestRate | noYears
# output = monthly payment | total payment

loanAmount = 100000
monthlyInterestRate = 0.01
noYears = 7

monthlypayment = (loanAmount * monthlyInterestRate) / ( 1 - (1 / (math.pow(1 + monthlyInterestRate, noYears * 12))))
totalpayment = monthlypayment * noYears * 12
print(monthlypayment, totalpayment)
print('monthlypayment = ', round(monthlypayment, 2))
print('totalpayment = ', round(totalpayment, 2 ))

