"""
Name: April Silva
lab13.py
"""

def is_in_binary(list, value):
    midpoint = list[len(list)//2]
    while midpoint != value and len(list) != 1:
        if value > midpoint:
            list = list[midpoint + 1:]
        else:
            list = list[:midpoint]
        midpoint = list[len(list)//2]
    if len(list) == 1 and list[0] != value:
        return False
    else:
        return True

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]

def calc_area(rect):
    p1 = rect.getp1()
    p2 = rect.getp2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]


def star_find(fn):
    file = open(fn, 'r')
    signals = file.read().split()
    found = []
    while signals != found: #loop through signals
        if signals >= 4000 and signals <= 5000:
            signals = signals + found
        if signals == 5:
            return True
    print(found)
    print("5 were not found")
    print(found)







def main():

    main()
