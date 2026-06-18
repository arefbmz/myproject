import random

name = input("ready player 1 , please write your names: ")
n = random.randint(1, 99)
while True:
    guess = int(input("please type your guess number: "))
    if guess == n:
        print("hey", name, "well done , you are amazing")
        break
    elif guess > n:
        print("its smaller than")
    elif guess < n:
        print("its biggest than")
