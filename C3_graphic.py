import os
import time

os.system("cls")

top_1 = "  " + "+" * 20 + "  "
top_2 = " +" + " " * 20 + "+ "

bot_1 = "+" + " " * 7 + "  _ _ " + " " * 9 + "+"
bot_2 = "+" + " " * 6 + " | O O |" + " " * 8 + "+"
bot_3 = "+" + " " * 6 + " | O O |" + " " * 8 + "+"

spacer = "+" + " " * 22 + "+"

field_6 = "+" + " " * 5 + " "*13 + " " * 5 + "+"

field_1 = "+" + " " * 5 + " 1 2 3 4 5 6 " + " " * 4 + "+"

player = "+" + " " * 5 + " 1 PLAYER 2 " + " " * 5 + "+"
player12_1 = "+" + " " * 4 + "XXX" * 2 + "  " + "YYY" * 2 + " " * 4 + "+"
player12_2 = "+" + " " * 4 + "XXX" * 2 + "  " + "YYY" * 2 + " " * 4 + "+"

cursor = "+ o> "

playing = True

c = 8  # center


def player_by_round(lvl, rnd, p):
    # print(lvl, rnd, p)

    if rnd > 11:
        if lvl == 1:
            no_a, no_b = 6, 6
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


def render_clean():
    os.system("cls")


def whoPlays(pl):
    status_s1 = "+" + " " * 4 + "^TURN" + " " * 13 + "+"
    status_s2 = "+" + " " * 12 + "^TURN" + " " * 5 + "+"

    return status_s1 if pl == 1 else status_s2


def bot_anim(row, step, flag):
    # print(row, step, flag)
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
        question = "+> SELECT COLUMN(1-6)" + " "*2
    elif mode == 1:
        question = "+> playing..\t" + " "*7
    else:
        question = "+> Watch your input!(1-6)"
    return question


def play_anim(r, p, row, mode, d):
    if d == 0:
        for e in range(4):
            render_view(r, p, row, mode, e)
            time.sleep(.08)
    else:
        for e in range(3, -1, -1):
            render_view(r, p, row, mode, e)
            time.sleep(.08)
    time.sleep(.2)


def anim_start():
    # set console color
    os.system("color f0")

    # Animation Start und Einstellung
    a, b, s = 11, 11, -1
    m = a + b

    welcome = [
        "+ " + "+ "*17 + "+",
        "+ + " + "  "*15 + "+ +",
        "+" + " "*6 + "T h e  O r i g i n a l " + " "*6 + "+",
        "+" + " "*9 + "C o n n e c t  3" + " "*10 + "+",
        "+" + " " * 13 + "G A M E" + " " * 15 + "+",
        "+" + " "*a + "<PrESS StART>" + " "*b + "+",
        "+ " + "+ " * 17 + "+"
    ]

    for e in range(42):
        render_clean()
        for w in welcome:
            print(w)

        a = a + s
        b = m - a

        if a <= 1 or a >= 21:
            s *= -1

        welcome[5] = "+" + " " * a + "<PrESS StART>" + " " * b + "+"

        time.sleep(.06)

    input(cursor + "<enter to start > ")

    return anim_selection()


def anim_cleanup():
    pass


def anim_win(no):
    time.sleep(2)

    print("\n")
    # render_clean()
    # Animation Ende und <ok> to start again

    out = [
        "+ "*11,
        "+  " + " Game finished " + "  +",
        "+  " + " " * 15 + "  +",
        "+ " + "  P L A Y E R  " + str(no) + "  +",
        "+  " + " "*4 + "W O N !" + " "*4 + "  +",
        "+  " + " " * 15 + "  +",
        "+ "*11,
    ]

    for e in out:
        print(e)

    input("\n> Press <enter> to exit..")

    # RESET CONSOLE COLOR


def anim_loading():
    # Loading Screen

    pass


def anim_selection():
    game, grav, start = -1, -1, -1

    # 0 - 6 (GAMEMODE), 7 - 11 (GRAVITY MODE), 12 - :-1 (PLAYER)
    ask = [
        "+ "*12,
        "+ [ SELECT GAMEMODE ] +",
        "+" + " "*21 + "+",
        "+ Human vs Human [1]  +",
        "+ Human vs Robot [2]  +",
        "+ Robot vs Robot [3]  +",

        "+ " * 12,
        "+ [ SELECT GRAVITY ]  +",
        "+" + " " * 21 + "+",
        "+ SET Gravity on  [1] +",
        "+ SET Gravity off [2] +",

        "+ " * 12,
        "+  [ SELECT PLAYER ]  +",
        "+" + " " * 21 + "+",
        "+ Player 1 (X) -> [1] +",
        "+ Player 2 (O) -> [2] +",
    ]

    # GAMEMODE
    render_clean()
    for e in ask[:6]:
        print(e)
    while game not in range(3):
        try:
            game = int(input(cursor))-1
        except ValueError:
            pass

    return game, 0, 0

    # GRAVITY MODE
    render_clean()
    for e in ask[6:11]:
        print(e)
    while grav not in range(2):
        try:
            grav = int(input(cursor))-1
        except ValueError:
            pass

    if game in [0, 1]:
        # STARTING PLAYER
        render_clean()
        for e in ask[11:-1]:
            print(e)
        while start not in range(1):
            try:
                start = int(input(cursor))-1
            except ValueError:
                pass
    else:
        start = 1

    return game, grav, start


def render_view(r, p, row, mode=0, s=0):
    render_clean()

    # ausgabe
    for level in [spacer[:-1] + spacer[c:-c] + spacer[1:],
                  field_1[:-1] + bot_1[c:-c] + player[1:],
                  format_row("A", row[0])[:-1] + bot_2[c:-c] + player_by_round(1, r, p)[1:],
                  format_row("B", row[1])[:-1] + bot_3[c:-c] + player_by_round(2, r, p)[1:],
                  format_row("C", row[2])[:-1] + bot_anim(1, s, p)[c:-c] + whoPlays(p)[1:],
                  format_row("D", row[3])[:-1] + bot_anim(2, s, p)[c:-c] + spacer[1:],
                  field_6[:-1] + bot_anim(3, s, p)[c:-c] + spacer[1:],
                  spacer[:-1] + spacer[c:-c] + spacer[1:],
                  quest_by_mode(mode) + spacer[c:-c] + spacer[1:]]:
        print(level)
    # time.sleep(.1)




#
# v2
# Bild übergeben an renderer mit func(grafik=[".."], values=[])
# grafik besteht aus ".....", ".    .", "..$..", $ for replace with value
# values besteht aus 4, 2, 5, 1, "Text", etc damit $ = 4
#
#
#
