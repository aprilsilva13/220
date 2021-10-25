"""
April Silva
weighted_average.py
Description: Homework 7
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    acc = 0
    students = 0
    for line in in_file:
        halves = line.split(":")
        grades = halves[1].strip().split()
        total_weight = 0
        total_grade = 0
        # Loop through grades, by
        for i in range(0, len(grades), 2):
            # weight is grades[i]
            weight = int(grades[i])
            # add that weight to a total weight
            total_weight += weight
        # if weight is less than 100 show an error
        if total_weight < 100:
            out_file.write(halves[0] + "'s average: " + "Error: The weights are less than 100.\n")
        # same for if its greater than 100
        elif total_weight > 100:
            out_file.write(halves[0] + "'s average: " + "Error: The weights are more than 100.\n")
        else:
            students += 1
            # if equal to 100, calculate the average for the current person
            for i in range(0, len(grades), 2):
                # grade is grades[i + 1]
                grade = int(grades[i + 1])
                # multiply weight by grade and add to a total grade
                # weight is grades[i]
                weight = int(grades[i])
                total_grade += (weight * grade)
            avg = total_grade / 100
            # total_grade / 100 and round to 1 decimal place
            avg = round(avg, 1)
            # add that to acc
            acc = acc + avg
            out_file.write(halves[0] + "'s average: " + str(avg) + "\n")
    # take acc and divide by the number of students and round to 1 decimal place
    if students == 0:
        acc = 0
    else:
        acc = round(acc / students, 1)
    out_file.write("Class average: " + str(acc) + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")

main()