"""
Name: April Silva.py
lab10.py
"""

def build_board():
    positionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return positionlist

def display_board(positionlist):
    print("----------")
    counter = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(positionlist[counter], end= "|")
            counter += 1
        print()
    print("----------")

def placespot(positionlist, spot, marker):
    positionlist[spot] = marker

def legal_spot(positionlist, spot):
    if (positionlist[spot] == "x" or positionlist[spot] == "o") or (spot < 1 or spot > 9):
        return False
    else:
        return True

def game_won(positionlist):
    winCon = [[1, 2, 3], [4, 5, 6,], [7, 8 ,9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        counter = 0
        for spot in condition:
            if positionlist[spot-1] == "x":
                counter += 1
            if counter == 3:
                return "x wins"
            if positionlist[spot-1] == "o":
                counter += 1
            if counter == 3:
                return "o wins"

def game_over(turncount, positionlist):
    if (game_won(positionlist) == "x wins") or (game_won(positionlist) == "o wins") or (turncount > 9):
        return True
    else:
        return False

def play_game():
    positionlist = build_board()
    display_board(positionlist)
    turncount = 1
    while not game_over(turncount, positionlist):
        xmark = eval(input("x, where will you place your mark?"))
        if legal_spot(positionlist, xmark):
            placespot(positionlist, spot, marker)
            turncount = turncount + 1
            display_board(positionlist)
        omark = eval(input("o, where will you place your mark?"))
        if legal_spot(positionlist, omark):
            placespot(positionlist, spot, marker)
            turncount = turncount + 1
            display_board(positionlist)
        if game_won(positionlist) == "x wins":
            print("x wins the game")
        if game_won(positionlist) == "o wins":
            print("o wins the game")


def main():
    play_game()


main()


