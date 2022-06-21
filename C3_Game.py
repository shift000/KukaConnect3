import random
import time

from C3_graphic import *


# INIT

# CUBE - spieler-ID(1/2), ausgespielt in runde x, pos auf spielbrett (X / Y)
class Cube:
    def __init__(self, p_id):
        self.player_id = p_id
        self.round_played = -1
        self.letter = -1
        self.number = -1

    def get_player(self):
        return self.player_id

    def is_empty(self):
        return True if self.player_id == -1 else False

    def is_player(self, pid):
        return True if self.player_id == pid else False

    def list_all(self):
        return self.player_id, self.round_played, self.letter, self.number


empty = "X"

# Array Spielfeld
arr_field = [
    [Cube(-1)] * 6,  # A
    [Cube(-1)] * 6,  # B
    [Cube(-1)] * 6,  # C
    [Cube(-1)] * 6,  # D
]

placed = []
moves = []
playing = True
gameround = 0
time2wait = 1
mode = 0


class Move:
    def __init__(self, r, A, B, C):
        self.r = r
        self.m = [A, B, C]


def place_cube(sign, number, letter=0):  # eg. place_cube("A", 4)

    for e in range(3, -1, -1):
        if arr_field[e][number - 1].is_empty():
            # print("found at %d %d" % (e,number))
            arr_field[e][number - 1] = Cube("X" if sign == "A" else "O")
            return [e, number - 1]


def shuffle():
    # sort ratings from 1 to 3
    temp = []

    for e in range(3):
        for m in moves:
            if m.r == str(e + 1):
                temp.append(m)

    # print(temp, moves)

    return temp


def listify_field(arr):
    ret = []
    print("STARTE")
    for r in arr:
        temp = ""
        for n in r:
            temp += ". " if n.get_player() == -1 else str(n.get_player()) + " "

        ret.append(temp)
    return ret


def make_move(sign):
    for e in moves:
        move = e.m

        # teste ob move möglich
        next_1 = move[1]
        next_2 = move[2]

        if arr_field[next_1[0]][next_1[1]] in (empty, sign) and arr_field[next_2[0]][next_2[1]] in (empty, sign):
            if arr_field[next_1[0]][next_1[1]] == sign:
                # platziere letzten
                return next_2[1]
            else:
                # platziere zweiten
                return next_1[1]

        else:  # move nicht mehr möglich, entferne
            # print("ENTFERNE %s" % e.m)
            moves.remove(e)

    # print("[A] random")
    return random.randint(0, 5)


def pp():
    for e in arr_field:
        print(e)


def pm():
    print("[A] POSSIBLE MOVES")
    for move in moves:
        print(move.r, " -> ", move.m)


def anim_get_cube(p):
    play_anim(gameround, p, listify_field(arr_field), mode, 0)


def anim_place_cube():
    play_anim(gameround, 0, listify_field(arr_field), mode, 1)


def poss_moves(Y, X):
    empty = -1
    xmin = 0
    xmax = 5
    ymin = 0
    ymax = 3

    # check center r = 1
    if xmin < X < xmax:
        if arr_field[Y][X - 1].is_empty() and arr_field[Y][X + 1].is_empty():
            if Y == ymax or not arr_field[Y + 1][X - 1].is_empty() and not arr_field[Y + 1][X + 1].is_empty():
                moves.append(Move("1", [Y, X], [Y, X - 1], [Y, X + 1]))

    # check left r = 2
    if X > xmin + 1:
        if arr_field[Y][X - 2].is_empty() and arr_field[Y][X - 1].is_empty():
            if Y == ymax or not arr_field[Y + 1][X - 2].is_empty() and not arr_field[Y + 1][X - 1].is_empty():
                moves.append(Move("2", [Y, X], [Y, X - 1], [Y, X - 2]))

    # check right r = 2
    if X < xmax - 1:
        if arr_field[Y][X + 1].is_empty() and arr_field[Y][X + 2].is_empty():
            if Y == ymax or not arr_field[Y + 1][X + 2].is_empty() and not arr_field[Y + 1][X + 1].is_empty():
                moves.append(Move("2", [Y, X], [Y, X + 1], [Y, X + 2]))

    # check top r = 2
    if Y > ymax - 2:
        if arr_field[Y - 1][X].is_empty() and arr_field[Y - 2][X].is_empty():
            moves.append(Move("2", [Y, X], [Y - 1, X], [Y - 2, X]))

    # check left strike r = 3
    if X > xmin + 1 and Y > ymin + 1:
        if arr_field[Y - 1][X - 1].is_empty() and arr_field[Y - 2][X - 2].is_empty():
            if not arr_field[Y][X - 1].is_empty() and not arr_field[Y - 1][X - 2].is_empty():
                moves.append(Move("3", [Y, X], [Y - 1, X - 1], [Y - 2, X - 2]))

    # check right strike	r = 3
    if X < xmax - 1 and Y > ymin + 1:
        if arr_field[Y - 1][X + 1].is_empty() and arr_field[Y - 2][X + 2].is_empty():
            if not arr_field[Y][X + 1].is_empty() and not arr_field[Y - 1][X + 2].is_empty():
                moves.append(Move("3", [Y, X], [Y - 1, X + 1], [Y - 2, X + 2]))

    # check left strike cube in center r = 3
    if X > xmin and Y < ymax - 1:
        if arr_field[Y - 1][X - 1].is_empty() and arr_field[Y + 1][X + 1].is_empty():
            if not arr_field[Y][X - 1].is_empty():
                moves.append(Move("3", [Y, X], [Y - 1, X - 1], [Y + 1, X + 1]))

    # check right strike in center	r = 3
    if X < xmax and Y < ymax - 1:
        if arr_field[Y - 1][X + 1].is_empty() and arr_field[Y + 1][X - 1].is_empty():
            if not arr_field[Y][X + 1].is_empty():
                moves.append(Move("3", [Y, X], [Y - 1, X + 1], [Y + 1, X - 1]))


def check_win(sign):
    for e in range(4):
        for t in range(4):
            if arr_field[e][t].is_player(sign):
                if arr_field[e][t + 1].is_player(sign):
                    if arr_field[e][t + 2].is_player(sign):
                        print("%s won !! " % sign)
                        return True

    for e in range(2):
        for t in range(6):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t].is_player(sign):
                    if arr_field[e + 2][t].is_player(sign):
                        print("%s won !! " % sign)
                        return True

    for e in range(2):
        for t in range(4):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t + 1].is_player(sign):
                    if arr_field[e + 2][t + 2].is_player(sign):
                        print("%s won !! " % sign)
                        return True

    for e in range(2):
        for t in range(2, 6):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t - 1].is_player(sign):
                    if arr_field[e + 2][t - 2].is_player(sign):
                        print("%s won !! " % sign)
                        return True

    return False


while playing:
    anim_get_cube(1)
    p_A = place_cube("A", make_move("A"))
    anim_place_cube()

    poss_moves(p_A[0], p_A[1])

    moves = shuffle()

    if check_win(1):
        playing = False
        continue

    gameround += 1

    anim_get_cube(2)
    print(gameround)
    p_B = place_cube("B", int(input(answer)))
    anim_place_cube()

    if check_win(2):
        playing = False
        continue

    gameround += 1

    print("\n\n")

pp()
