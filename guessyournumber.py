print("I can guess your number you choose between 1-100 in under 10 guesses\n")


print("After every guess input:\ny if it is your number \nor nb if your number is bigger \nor ns if your number is smaller")

numbers = [t for t in range(1,103)]
guessamo = 0

#uses binary search algotrithm to find number
def guess():
    global guessamo
    global numbers 
    guessamo += 1
    num_guess = int(len(numbers)/2)
    res = input("Is this your {} number?: ".format(numbers[num_guess]))
    if res.lower() == 'y':
        return 0
    elif res.lower() == 'nb':
        numbers = numbers[num_guess:]
        guess()
    else:
        numbers = numbers[:num_guess]
        guess()

guess()
print("Told You I could do it. It took me {} guesses".format(guessamo))
