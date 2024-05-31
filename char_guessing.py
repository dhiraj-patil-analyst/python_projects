import random

name=input("What is your name:-")
print('Good Luck:-',name)


words=['Suraj','Teja','Aai','Prem','Reshma','Roy','Manisha','Shiva','Veera','Mahesh','Richa','Pappa','Barshi','Solapur']
word=random.choice(words)
#print(word)
print('Guess The Character:-')
guesses=''
turns=5
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print('_')
            failed+=1
    if failed==0:
        print("You Win!",name)
        print("The Word is:",word)
        break
    print() 
    guess=input("guess a character:")
    guesses+=guess
    if guess not in word:
       turns-=1
       print('Wrong')
       print("You have",+turns,'more guesses')
    if turns==0:
       print("Your loose",name)