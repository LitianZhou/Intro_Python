from random import randint

print("This is the basic game")
car = randint(1, 3)
guess = int(input("Guess among 1,2,3: "))

print("The car was behind Door #" + str(car))
print("You picked Door #" + str(guess))

print("---------This is the second game-------------")
car = randint(1, 3)
guess = int(input("Guess among 1,2,3: "))

if guess == car:
    rev = car+1
    if rev == 4:
        rev = 1
    # pre-set changeTo door
    if car+rev == 3:
        changeTo = 3
    elif car+rev == 4:
        changeTo = 1
    elif car+rev == 6:
        changeTo = 2
    else:
        print("Error1, exception throws")
else:   # guess is wrong
    if car+guess == 3:
        rev = 3
        
    elif car+guess == 4:
        rev = 2
    elif car+guess == 5:
        rev = 1
    else:
        print("Error2, you might choose an invalid guess")
    changeTo = car
print("Door #"+str(rev)+" hides a goat")
changeFlag = input("Would you like to change your guess? type in yes or no: ")
if changeFlag.lower() == "yes":
    guess = changeTo

# print result
print("The car was behind Door #"+str(car))
if car == guess:
    print("You win!")
else:
    print("You lost.")


print("---------This is part 3 -----------")
while True:
    repetition = int(input("How many rounds of the game should be simulated?"))
    if repetition < 10 or repetition > 10000:
        print("Must enter a number between 10 and 10000")
        print("Please try again:")
    else:
        break
changeFlag = input("Switch or not? Input yes or no.").lower()

win = 0
for i in range(repetition+1):
    car = randint(1, 3)
    guess = randint(1, 3)
    
    if guess == car:
        rev = car+1
        if rev == 4:
            rev = 1
        # pre-set changeTo door
        if car+rev == 3:
            changeTo = 3
        elif car+rev == 5:
            changeTo = 1
        elif car+rev == 4:
            changeTo = 2
        else:
            print("Error1, exception throws")
    else:  # guess is wrong
        if car+guess == 3:
            rev = 3
            
        elif car+guess == 4:
            rev = 2
        elif car+guess == 5:
            rev = 1
        else:
            print("Error2, you might choose an invalid guess")
        changeTo = car

    if changeFlag.lower() == "yes":
        guess = changeTo

    # scoreboard:
    if car == guess:
        win += 1
print("The player won " + str(win) + "/" + str(repetition) + " games. " + format(win/repetition, '.4%'))


    