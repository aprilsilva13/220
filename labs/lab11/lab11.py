"""
Name: April Silva
lab11.py
"""
from random import *

def words(ifn):
    infile = open(ifn, "r")
    contents = infile.read()
    return contents.split("\n")

def random_word(lst):
    return lst[randint(0, len(lst) - 1)]

def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
        return "".join(secret)

def won(word, letters):
    x = fill(word, letters)
    if word == x:
        return True
    else:
        return False

def play():
    list_words = words("wordlist.txt")
    secret = random_word(list_words)
    incorrect = 0
    guesses = []
    current = "_" * len(secret)
    while incorrect < 7 and not won(secret, guesses):
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("what is the letter?")
        while letter in guesses:
            letter = input("What is the letter?")
        guesses.append(letter)
        display = fill(secret, guesses)
        if current == display:
            incorrect += 1
        else:
            current = display


def main():
    play()

main()

