import random


playtotal = 1

def check(guess):
    while True:
        try:
            guess = int(guess)
            1<=guess and guess<=100
            break
        except:
            if guess == "hint" or guess == "hack":
                break
            else:
                print("Wrong input, Try again")
                guess = input("Number: ")
    return guess

def main():
    print("I'm thinking of an integer between 1-100")
    guess = input("What's your guess: ")
    magic = int(random.randint(1,100))
    score = 1
    hints = 3
    global playtotal
    playtotal+=1
    check(guess)


    while guess != magic   :
        guess = str(guess)
        if guess.lower() == "hint" and hints > 0:
            hints -= 1
            if last > magic:
                print("Think of a number that is smaller")
                guess = str(input("What's your guess: "))
                guess = check(guess)
            else:
                print("Think of a number that is bigger")
                guess = str(input("What's your guess: "))
                guess = check(guess)
                
        elif guess.lower() == 'hack':
            print(magic)
            break
        else:
            score +=1
            print("Sorry that's wrong")
            last = int(guess)
            if hints > 0 and score > 2:
                if hints == 3:
                    hintleft = "hints left"
                elif hints == 2:
                    hintleft = "hints"
                else:
                    hintleft = "hint left"
                print("You have {} {} that you can use by typing hint".format(hints, hintleft))
            guess = input("What's your guess: ")
            guess = check(guess)
            
            

    print("Congrats it took you {} guesses".format(score))
    

main()


#play again function
ans = input("Do you want to play again Y/N: ")

while ans.lower() == 'y':
    print("This is your {} game".format(playtotal))
    main()
    ans = input("Do you want to play again Y/N: ")

if playtotal > 1:
    game = "games"
else:
    game = "game"
print("Thank you for playing {} {}".format(playtotal, game))




