import os
import time

os.system("cls")

top_1 = "  " + "+" * 20 + "  "
top_2 = " +" + " " * 20 + "+ "

bot_1 = "+" + " " * 7 + "  _ _ " + " " * 9 + "+"
bot_2 = "+" + " " * 6 + " | O O |" + " " * 8 + "+"
bot_3 = "+" + " " * 6 + " | O O |" + " " * 8 + "+"

spacer = "+" + " " * 22 + "+"

field_1 = "+" + " " * 5 + " F I E L D # " + " " * 4 + "+"

field_6 = "+" + " " * 5 + " 1 2 3 4 5 6 " + " " * 5 + "+"

player = "+" + " " * 5 + " 1 PLAYER 2 " + " " * 5 + "+"
player12_1 = "+" + " " * 4 + "XXX" * 2 + "  " + "YYY" * 2 + " " * 4 + "+"
player12_2 = "+" + " " * 4 + "XXX" * 2 + "  " + "YYY" * 2 + " " * 4 + "+"

answer = "+ o>" + " " * 2

playing = True

c = 8  # center


def player_by_round(lvl, rnd, p):
    # print(lvl, rnd, p)

    if rnd > 11:
        if lvl == 1:
            no_a, no_b = 0, 0
        else:
            if (rnd - 12) % 2 != 0:
                no_a = int((rnd - 12 + 1) / 2)
                no_b = no_a
            else:
                no_b = int((rnd - 12) / 2)
                no_a = no_b + 1
    else:
        if lvl == 1:
            if rnd % 2 != 0:
                no_a = int((rnd + 1) / 2)
                no_b = no_a
            else:
                no_b = int(rnd / 2)
                no_a = no_b + 1
        else:
            no_a, no_b = 0, 0

    # print("-> ", no_a, no_b)

    return "+" + " " * 4 + "." * no_a + "X" * (6 - no_a) + "  " + "." * no_b + "O" * (6 - no_b) + " " * 4 + "+"


def format_row(row, arr):
    field_2 = "+" + " " * 4 + row + " " + arr + " " * 4 + "+"

    return field_2


def whoPlays(pl):
    status_s1 = "+" + " " * 4 + "PLAYS" + " " * 13 + "+"
    status_s2 = "+" + " " * 12 + "PLAYS" + " " * 5 + "+"

    return status_s1 if pl == 1 else status_s2


def bot_anim(row, step, flag):
    flag = " " if flag == 0 else "X" if flag == 1 else "O"
    bot_4 = ["+" + " " * 7 + " ||   " + " " * 9 + "+",
             "+" + " " * 7 + " //   " + " " * 9 + "+",
             "+" + " " * 9 + "  \\\\  " + " " * 7 + "+",
             "+" + " " * 9 + "   || " + " " * 7 + "+"]

    bot_5 = ["+" + " " * 7 + "  \\_->" + flag + " " * 8 + "+",
             "+" + " " * 7 + "/ " + " " * 13 + "+",
             "+" + " " * 11 + " /" + " " * 9 + "+",
             "+" + " " * 8 + flag + "<-_/  " + " " * 7 + "+"]

    bot_6 = ["+" + " " * 7 + " " * 7 + " " * 7 + "+",
             "+" + " " * 7 + "\\->" + flag + " " * 10 + "+",
             "+" + " " * 8 + flag + "<-/" + " " * 9 + "+",
             "+" + " " * 8 + " " * 7 + " " * 6 + "+"]

    if row == 1:
        return bot_4[step]
    elif row == 2:
        return bot_5[step]
    else:
        return bot_6[step]


def quest_by_mode(mode):
    if mode == 0:
        question = "+> SELECT COLUMN(1-6)" + " " * 2 + "+"
    else:
        question = "+> SELECT ROW(A-D)" + " " * 5 + "+"
    return question


def play_anim(r, p, row, mode, d):
    if d == 0:
        for e in range(4):
            render_view(r, p, row, mode, e)
            time.sleep(.2)
    else:
        for e in range(3, -1, -1):
            render_view(r, p, row, mode, e)
            time.sleep(.2)
    time.sleep(.3)


def render_view(r, p, row, mode=0, s=0):
    os.system("cls")

    # ausgabe
    for level in [spacer[:-1] + spacer[c:-c] + spacer[1:],
                  field_1[:-1] + bot_1[c:-c] + player[1:],
                  format_row("A", row[0])[:-1] + bot_2[c:-c] + player_by_round(1, r, p)[1:],
                  format_row("B", row[1])[:-1] + bot_3[c:-c] + player_by_round(2, r, p)[1:],
                  format_row("C", row[2])[:-1] + bot_anim(1, s, p)[c:-c] + whoPlays(p)[1:],
                  format_row("D", row[3])[:-1] + bot_anim(2, s, p)[c:-c] + spacer[1:],
                  field_6[:-1] + bot_anim(3, s, p)[c:-c] + spacer[1:],
                  spacer[:-1] + spacer[c:-c] + spacer[1:],
                  quest_by_mode(mode)[:-1] + spacer[c:-c] + spacer[1:]]:
        print(level)
    time.sleep(.1)
