import random
randNumber=random.randint(1,100)
userGuess=None
guesses=1
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess"))
    if(userGuess>randNumber):
      print("lower Number please!")
      guesses+=1
    else:
      print("Higher Number please!")
      guesses+=1
if(userGuess==randNumber):
    print("you guessed it right!")
print(f"Number of guesses is {guesses}")



