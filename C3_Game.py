import random
import time
import sys

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


class KI:
    def __init__(self, sign):
        self.moves = []
        self.sign = sign

    def get_moves(self):
        return

    def check_center(self, arr):
        r = -1
        if len(arr) > 1:
            for e in arr[1:]:
                r = self.move_center(arr[0], e)
                if r != -1:
                    break

            if r == -1:
                r = self.check_center(arr[1:])
        return r

    def check_next(self, arr):
        r = -1
        if len(arr) > 1:
            for e in arr[1:]:
                r = self.move_next(arr[0], e)
                if r != -1:
                    break

            if r == -1:
                r = self.check_next(arr[1:])
        return r

    def move_center(self, in_a, in_b):
        # print(self.sign, in_a, " -> ", in_b)
        x1 = (in_a[0] - in_b[0]) / 2
        x2 = (in_a[1] - in_b[1]) / 2

        ret = -1

        if [x1, x2] in [[1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]:  # X _ X
            spalte, reihe = int(in_a[0] + (x1 * -1)), int(in_a[1] + (x2 * -1))

            if arr_field[reihe][spalte].is_empty():
                if reihe == 3 or arr_field[reihe + 1][spalte].player_id in ["X", "O"]:
                    ret = [spalte + 1, reihe + 1]
            else:
                ret = -1

        # print(self.sign, x1, x2, [x1, x2] in [[-1, 1], [1, 1], [-1, 0]], " => ", ret)

        return ret

    def move_next(self, in_a, in_b):
        mi, ma = min(in_a, in_b), max(in_a, in_b)

        x1 = (mi[0] - ma[0]) / 2
        x2 = (mi[1] - ma[1]) / 2

        a_x = mi[0]
        a_y = mi[1]

        b_x = ma[0]
        b_y = ma[1]

        ret = -1

        # INFO : arr_field [ Y ][ X ]

        # SIDE
        if [x1, x2] in [[-0.5, 0], [0.5, 0]]:
            if logging:
                print("SIDE ", mi, ma)

            if 0 < a_x < 5 and 0 < a_y <= 3:
                if arr_field[a_y][a_x - 1].is_empty() and (
                        a_y == 3 or not arr_field[a_y + 1][a_x - 1].is_empty()):  # _XX
                    if logging:
                        print("LEFT ", a_x - 1, a_y + 1)

                    return [a_x, a_y]
            if 0 < b_x < 5 and 0 < b_y <= 3:
                if arr_field[b_y][b_x + 1].is_empty() and (
                        b_y == 3 or not arr_field[b_y + 1][b_x + 1].is_empty()):  # XX_
                    if logging:
                        print("RIGHT ", b_x + 2, b_y)

                    return [b_x + 2, b_y]

        # TOP
        if [x1, x2] in [[0, -0.5], [0, 0.5]]:  # top
            if logging:
                print("TOP ", mi, ma)

            if a_y > 0 and arr_field[a_y - 1][a_x].is_empty():
                return [a_x + 1, a_y - 1]

        # SCHRAEG RECHTS
        if [x1, x2] in [[0.5, -0.5], [-0.5, 0.5]]:  # left side
            if logging:
                print("Right SIDE  - CHECK ", mi, " and ", ma)

            if b_x < 5 and b_y > 0:
                if logging:
                    print("TOP - NEXT ", [b_x + 2, b_y - 1], " DOWN ", [b_x + 1, b_y])

                if arr_field[b_y - 1][b_x + 1].is_empty() and not arr_field[b_y][b_x + 1].is_empty():
                    # return [b_y - 1, b_x + 1]
                    return [b_x + 2, b_y - 1]
            elif b_x < 5 and b_y < 2:
                if logging:
                    print("BOTT - NEXT ", [a_x - 1, a_y + 1], " DOWN ", [a_x - 1, a_y + 2])

                if arr_field[a_y + 1][a_x - 1].is_empty() and not arr_field[a_y + 2][a_x - 1].is_empty():
                    return [a_x, a_y + 1]

        # SCHRAEG LINKS
        if [x1, x2] in [[-0.5, -0.5], [0.5, 0.5]]:  # right side
            if logging:
                print("Left SIDE  - CHECK ", mi, " and ", ma)

            if a_x > 0 and 0 < a_y < 3:
                if logging:
                    print("TOP - NEXT ", [a_x - 1, a_y - 1], " DOWN ", [a_x - 1, a_y])

                if arr_field[a_y - 1][a_x - 1].is_empty():
                    if a_y == 3 or not arr_field[a_y][a_x - 1].is_empty():
                        return [a_x, a_y - 1]
            elif b_x < 5 and 0 < b_y < 3:
                if logging:
                    print("BOTT - NEXT ", [b_x + 1, b_y + 1], " DOWN ", [b_x + 1, b_y + 2])

                if arr_field[b_y + 1][b_x + 1].is_empty():
                    if b_y + 1 == 3 or not arr_field[b_y + 2][b_x + 1].is_empty():
                        return [b_x + 2, b_y + 2]

        if logging:
            print(self.sign, x1, x2, [x1, x2] in [[-1, 1], [1, 1], [-1, 0]], " => ", ret)

        return [ret[0] + 1, ret[1] + 1] if ret != -1 else -1

    def move_random(self):
        rng = []
        for a_y in arr_field:
            no = 1
            for a_x in a_y:
                if a_x.is_empty():
                    if no not in rng:
                        rng.append(no)
                no += 1
        if rng:
            print("RAND => ", rng)
            time.sleep(.8)
            return rng[random.randint(0, len(rng) - 1)]
        else:
            # FIELD FULL - You made it till there?
            return -1

    def make_move(self):
        if logging:
            print("[%s] MAKING MOVE" % self.sign)

        placed_enemy = []
        placed_me = []
        pointer = [0, 0]

        for e in arr_field:
            ln = ""
            pointer[0] = 0
            for t in e:
                if t.player_id != -1:
                    if t.player_id != self.sign:
                        ln += "!"
                        placed_enemy.append([pointer[0], pointer[1]])
                    else:
                        ln += "$"
                        placed_me.append([pointer[0], pointer[1]])
                else:
                    ln += "."
                pointer[0] += 1
            pointer[1] += 1
            # print(ln)

        time.sleep(.2)

        return_move = -1

        # TODO : CHECK IF I COULD WIN - PRIO 1
        if return_move == -1:
            if logging:
                print("CHECK FOR ME")
            if len(placed_me) > 1:
                return_move = self.check_center(placed_me)
                if return_move == -1:
                    return_move = self.check_next(placed_me)
            if return_move != -1:

                if logging:
                    print("[%s] => PLACING %s" % (self.sign, return_move))
                return [self.sign, return_move[0]]

        # TODO : CHECK IF ENEMY COULD WIN - PRIO 2
        if return_move == -1:
            if logging:
                print("CHECK FOR ENEMY")
            if len(placed_enemy) > 1:  # in center X _ X
                return_move = self.check_center(placed_enemy)
                if return_move == -1:  # next X X _
                    return_move = self.check_next(placed_enemy)
            if return_move != -1:

                if logging:
                    print("[%s] => PLACING %s" % (self.sign, return_move))
                return [self.sign, return_move[0]]

        # TODO : PLACE RANDOM - PRIO 3
        if return_move == -1:
            if logging:
                print("RANDOM")
            return_move = self.move_random()

        time.sleep(.2)

        if logging:
            print("[%s] => PLACING %s" % (self.sign, return_move))

        return [self.sign, return_move]


class Player:
    def __init__(self, sign):
        self.sign = sign

    def make_move(self):
        inp = -1
        while inp not in [1, 2, 3, 4, 5, 6]:
            try:
                inp = int(input(cursor))
            except ValueError:
                pass
        return [self.sign, inp]


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
logging = True

list_player = []

log = []


def write_log():
    lf = "log.file"
    lh = open(lf, "w+")
    lh.seek(0)
    for e in log:
        lh.write(e)
    lh.close()


class Move:
    def __init__(self, r, A, B, C):
        self.r = r
        self.m = [A, B, C]


def place_cube(sign, number, letter=0):  # eg. place_cube("A", 4)

    for e in range(3, -1, -1):
        if arr_field[e][number - 1].is_empty():
            # print("found at %d %d" % (e,number))
            arr_field[e][number - 1] = Cube(sign)
            return [e, number - 1]
    return -1


def listify_field(arr):
    ret = []
    for r in arr:
        temp = ""
        for n in r:
            temp += ". " if n.get_player() == -1 else str(n.get_player()) + " "

        ret.append(temp)
    return ret


def anim_get_cube(p, tp):
    play_anim(gameround, p, listify_field(arr_field), tp, 0)


def anim_place_cube(tp):
    play_anim(gameround, 0, listify_field(arr_field), tp, 1)


def check_win(sign):
    for e in range(4):
        for t in range(4):
            if arr_field[e][t].is_player(sign):
                if arr_field[e][t + 1].is_player(sign):
                    if arr_field[e][t + 2].is_player(sign):
                        return True

    for e in range(2):
        for t in range(6):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t].is_player(sign):
                    if arr_field[e + 2][t].is_player(sign):
                        return True

    for e in range(2):
        for t in range(4):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t + 1].is_player(sign):
                    if arr_field[e + 2][t + 2].is_player(sign):
                        return True

    for e in range(2):
        for t in range(2, 6):
            if arr_field[e][t].is_player(sign):
                if arr_field[e + 1][t - 1].is_player(sign):
                    if arr_field[e + 2][t - 2].is_player(sign):
                        return True

    return False


if len(sys.argv) > 1:
    gm = int(sys.argv[1])

    if gm in [1, 2, 3]:
        game_mode, grav_mode, curr_player = gm-1, 0, 0
    else:
        print("Usage :")
        print("python C3_Game.py <gm>")
        print("for <gm>")
        print("1 Human vs. Human")
        print("2 Human vs. Robot")
        print("3 Robot vs. Robot")

        os.system("color 0f")
        exit()
else:
    game_mode, grav_mode, curr_player = anim_start()

list_player = [Player("X"), Player("O")] if game_mode == 0 else [Player("X"), KI("O")] if game_mode == 1 else [KI("X"),
                                                                                                               KI("O")]
anim_loading()

time_started = time.time()

while playing:
    for step in range(2):
        if playing:
            pla = list_player[curr_player]

            anim_get_cube(step + 1, 1 if type(pla) == KI else 0)

            x = list_player[curr_player].make_move()

            a = place_cube(x[0], x[1])
            loop_breaker = 2
            while a == -1:
                print(quest_by_mode(2))
                x = list_player[curr_player].make_move()
                a = place_cube(x[0], x[1])

                if loop_breaker <= 0:
                    if logging:
                        print("loop detected")
                    time.sleep(5)
                else:
                    loop_breaker -= 1
#
            anim_place_cube(1 if type(pla) == KI else 0)

            if check_win(list_player[curr_player].sign):
                anim_cleanup()

                print("+\n+ [i] Finished in [ %s ] sec" % round(time.time() - time_started, 2))

                anim_win(step + 1)
                playing = False

                # Exit Program, return cmd color
                os.system("color 0f")
                exit()
            else:
                curr_player = 1 if curr_player == 0 else 0
                gameround += 1

                time.sleep(.2)
        else:

            anim_win(step + 1)
exit()
