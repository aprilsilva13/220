"""
Name: April Silva
lab8.py
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file_name = open(in_file_name, "r")
    out_file_name = open(out_file_name, "w+")
    i = 1
    for line in in_file_name:
        words = line.split()
        for word in words:
            out_file_name.write(str(i) + " " + word + "\n")
            i += 1
    in_file_name.close()
    out_file_name.close()

def hourly_wages(in_file_name, out_file_name):
    in_file_name = open(in_file_name, "r")
    out_file_name = open(out_file_name, "w+")
    for line in in_file_name:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * int(parts[3])
        out_file_name.write(parts[0] + " " + parts[1] + " " + str(wage))


def calc_check_sum(isbn_str):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc += int(isbn_str[i]) * position
    return acc


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(line)

def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(file_name, friend_name, pad):
    padfile = open(pad, "r")
    key = padfile.read()
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("Walrus.txt", "wout.txt")
    hourly_wages("hourly_wages.txt", "wagesout.txt")
    send_message("message.txt", "lin")
    send_safe_message("secret_message.txt", "bob", 2)
    send_uncrackable_message("safest_message.txt", "bob", "pad.txt")
main()
