"""
Name: April Silva
Partner: <your partner's name goes here – first and last>
lab7.py
"""

import math

def cash_conversion():
    integer = eval(input("Enter an integer to be translated to a dollar amount: "))
    print("${:.2f}".format(integer))

def encode():
    x = eval(input("Enter a string: "))
    key = eval(input("Enter a key: "))
    acc = ""
    for i in range(x):
        y = ord(i)
        a = i + key
        character = chr(a)
        new_character = chr(a) + acc
    print(acc)

def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3
    return acc

def encode_better():
    m = eval(input("Enter a string: "))
    n = eval(input("Enter a key: "))
    acc = ""
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(n[i])
        result = c + key - 97
        acc += chr(result)
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(5))
    print(sum_n_cubes(4))
    encode_better()

main()
