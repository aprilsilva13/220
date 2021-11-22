"""
Name: April Silva
<lab12>.py

"""
from random import randint

def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list = ["April"]
    except:
        pass


def read_data(int):
    f = open(int, 'r')
    data = f.read()
    data = data.split()
    return data

def is_in_linear(val, values):
    i = 0
    while i < len(values):
        if i == val:
            return True
        i += 1
    else:
        return False

def good_input():
    x = eval(input("Enter a number: "))
    while x < 1 or x > 10:
        x = eval(input("Enter a number again: "))
    return x


def num_digits():
    num = eval(input("What is the number? "))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print("There were" + str(digits) + "digits")
        num = eval(input("What is the next number? "))

def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("Guess a number: "))
    while num != secret and guess != 7:
        guess += 1
        if num > secret:
            print("Too high!")
        else:
            print("Too low!")
        num = eval(input("Guess another number: "))
    if guess == secret:
        print("You won in" + str(guess) + "guesses!")
    else:
        print("Sorry, you lost! The number was " + str(secret))





def main():
    hi_lo_game()

main()
