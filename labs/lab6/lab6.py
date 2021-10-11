"""
Name: April Silva
lab6.py
"""

def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    #last_first = last + ", " + first
    print(last + "," + first)

def company_name():
    company = input("Enter a three-part internet domain:")
    company = company.split(".")
    print(company[1])


def initials():
    names = eval(input("Enter the # of names of students in a class: "))
    for i in range(names):
        firstname = input("What is the first name of the student? ")
        lastname = input("What is the last name of the student? ")
        print(firstname[0] + lastname[0])


def names():
    name = input("Enter first and last names: ")
    name = name.split(",")
    for n in name:
        # split at spaces
        name = name.split(" ")
    print(name)

def thirds():
    sentence = eval(input("Enter a sentence: "))
    for i in range(sentence):
        print(sentence[:3])


def word_average():
    sentence = eval(input("Enter a sentence: "))
    sentence = sentence.split()
    acc = 0
    for word in sentence:
        acc += len(word)
    print(acc / len(sentence))

def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence = sentence.split()
    for word in sentence:
        print(word[1:] + word[0] + "ay", end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

    # add other function calls here


main()
