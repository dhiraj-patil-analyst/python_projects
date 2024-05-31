# password generator
import random
print("Welcome to password generator:")
chars='abcdedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_.,?'
number=input("Number of passwords to generate:")
number = int(number)
length=input("Length of password:")
lenth=int(length)
print('\nHere your passwords:')

for i in range(number):
  passwords=''
  for c in range(lenth):
    passwords+=random.choice(chars)
  print(passwords)
