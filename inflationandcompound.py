#inflation and compound interest formula


def inflation(amount,time):
    while time > 0:
        sub = amount * .03
        amount -= sub
        time -=1
    return amount

def compound(amount,rate,time):
    A = amount*(1+(rate/100))**time
    return A

q = input("Compound interest or Inflation: ")

if q.lower() == 'inflation':
    amount = float(input("What's the inital amount? "))
    time = int(input("How many years: "))
    print(inflation(amount,time))
elif q.lower() == 'compound interest':
    amount = float(input("What's the inital amount? "))
    rate = float(input("What is the interest rate? "))
    time = int(input("How many years: "))
    print(compound(amount,rate,time))
