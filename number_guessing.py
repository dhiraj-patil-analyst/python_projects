import random
import math
 
upper_bound=int(input("Enter upper bound:"))
lower_bound=int(input("Enter lower bound:"))

x=random.randint(lower_bound,upper_bound)

count=0

while count<math.log(upper_bound-lower_bound+1,2):
    count+=1
    guess=int(input("Guess the number:"))
    if guess==x:
        print("You win the game in",count,"try")
    elif guess>x:
        print("Your are guessed too high")
    elif guess<x:
        print("Your are guessed too small")  


if count>math.log(upper_bound-lower_bound+1,2):
    print('\nthe number is',x)
    print('\tBetter luck next time')        