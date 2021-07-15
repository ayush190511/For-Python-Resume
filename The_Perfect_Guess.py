import random
randNumber = random.randint(1, 100)


userGuess= None
guesses = 0 

while(userGuess != randNumber):
    userGuess = int(input("Enter Your guess: "))
    guesses+=1
    if userGuess==randNumber:
        print ("your guessed it right!\n")
    else:
        if (userGuess>randNumber):
            print ("You guessed it wrong! Enter a smaller number")

        else:
            print ("You guessed it wrong! Enter a larger number") 
        

print(f"You guessed the number in {guesses} guesses")
with open ("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("you have just broken the high score") 
    with open ("hiscore.txt", "w") as f:
        f.write(str(guesses))