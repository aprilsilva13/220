"""
April Silva
mean.py
Description: Solving for means for HW 3
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
import math
def main():
    values = eval(input("Enter the number of values to be entered: "))
    sum = 0
    for i in range(values):
        input_values = eval(input("Enter value: " ))
        sum = input_values ** 2 + sum
        harmonic = 1 / input_values * 5
        geo = input_values ** (1/values)
    sum = math.sqrt(sum / values)
    harmonic = values / harmonic
    geo = math.sqrt(input_values ** 2)
    print(sum)
    print(harmonic)
    print(geo)


if __name__ == '__main__':
        main()
