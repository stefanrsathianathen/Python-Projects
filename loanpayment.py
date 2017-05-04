#loan payment calculator


amo = float(input("What's the loan amount? "))
rate = float(input("What's the interest rate (%)? "))
n = int(input("How many months? "))

r = rate/100


p = (r*(amo))/(1-(1 + r) **-n)

print(p)