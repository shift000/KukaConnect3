import random, time

# INIT

# CUBE - spieler-ID(1/2), ausgespielt in runde x, pos auf spielbrett (X / Y)
class Cube:
	def __init__(self, p_id):
		self.player_id = p_id
		self.round_played = -1
		self.letter = -1
		self.number = -1
		
empty = "X"
		
# Array Spielfeld
arr_field = [
	[empty]*6,	# A
	[empty]*6,	# B
	[empty]*6,	# C
	[empty]*6,	# D
]

placed = []
moves = []
playing = True
gameround = 0
time2wait = 1

class Move:
	def __init__(self, r, A, B, C):
		self.r = r
		self.m = [A, B, C]

	
def place_cube(sign, number, letter=0):	# eg. place_cube("A", 4)
	
	for e in range(3, -1, -1):
		if arr_field[e][number] == empty:
			#print("found at %d %d" % (e,number))
			arr_field[e][number] = sign
			return [e, number]

	
def shuffle():
	# sort ratings from 1 to 3
	temp = []
	
	for e in range(3):
		for m in moves:
			if m.r == str(e+1):
				temp.append(m)		

	#print(temp, moves)
	
	return temp
	
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
				#platziere zweiten
				return next_1[1]
				
		else: # move nicht mehr möglich, entferne
			print("ENTFERNE %s" % e.m)
			moves.remove(e)
		
	print("[A] random")
	return random.randint(0, 5)
		

	
def pp():
	for e in arr_field:
		print(e)
		
def pm():
	print("[A] POSSIBLE MOVES")
	for move in moves:
		print(move.r, " -> ", move.m)
			
	
	
def poss_moves(Y, X):
	empty = "X"
	xmin = 0
	xmax = 5
	ymin = 0
	ymax = 3

	# check center r = 1
	if xmin < X < xmax:
		if arr_field[Y][X-1] == empty and arr_field[Y][X+1] == empty:
			if Y == ymax or arr_field[Y+1][X-1] != empty and arr_field[Y+1][X+1] != empty:
				moves.append( Move("1", [Y, X], [Y, X-1], [Y, X+1] ) )
	
	# check left r = 2
	if X > xmin + 1:
		if arr_field[Y][X-2] == empty and arr_field[Y][X-1] == empty:
			if Y == ymax or arr_field[Y+1][X-2] != empty and arr_field[Y+1][X-1] != empty:
				moves.append( Move("2", [Y, X], [Y, X-1], [Y, X-2] ) )
	
	# check right r = 2
	if X < xmax - 1 :
		if arr_field[Y][X+1] == empty and arr_field[Y][X+2] == empty:
			if Y == ymax or arr_field[Y+1][X+2] != empty and arr_field[Y+1][X+1] != empty:
				moves.append( Move("2", [Y, X], [Y, X+1], [Y, X+2] ) )
	
	# check top r = 2
	if Y > ymax - 2 :
		if arr_field[Y-1][X] == empty and arr_field[Y-2][X] == empty:
			moves.append( Move("2", [Y, X], [Y-1, X], [Y-2, X] ) )
	
	# check left strike r = 3
	if X > xmin + 1 and Y > ymin + 1:
		if arr_field[Y-1][X-1] == empty and arr_field[Y-2][X-2] == empty:
			if arr_field[Y][X-1] != empty and arr_field[Y-1][X-2] != empty:
				moves.append( Move("3", [Y, X], [Y-1, X-1], [Y-2, X-2] ) )
	
	# check right strike	r = 3
	if X < xmax - 1 and Y > ymin + 1:
		if arr_field[Y-1][X+1] == empty and arr_field[Y-2][X+2] == empty:
			if arr_field[Y][X+1] != empty and arr_field[Y-1][X+2] != empty:
				moves.append( Move("3", [Y, X], [Y-1, X+1], [Y-2, X+2] ) )
	
	
def check_win(sign):
	for e in range(4):
		for t in range(4):
			if arr_field[e][t] == sign:
				if arr_field[e][t+1] == sign:
					if arr_field[e][t+2] == sign:
						print("%s won !! " % sign)
						return True
						
	for e in range(2):
		for t in range(6):
			if arr_field[e][t] == sign:
				if arr_field[e+1][t] == sign:
					if arr_field[e+2][t] == sign:
						print("%s won !! " % sign)
						return True
						
	for e in range(2):
		for t in range(4):
			if arr_field[e][t] == sign:
				if arr_field[e+1][t+1] == sign:
					if arr_field[e+2][t+2] == sign:
						print("%s won !! " % sign)
						return True
						
	for e in range(2):
		for t in range(2, 6):
			if arr_field[e][t] == sign:
				if arr_field[e+1][t-1] == sign:
					if arr_field[e+2][t-2] == sign:
						print("%s won !! " % sign)
						return True
						
	return False

	
print("\n" + "# "*20 + "\n")

x = place_cube("A", random.randint(0, 5))
poss_moves(x[0], x[1])
pm()

pp()
print("\n")

time.sleep(time2wait)


while playing:
	print(" ########### ROUND %d ########### " % gameround)
	
	p_B = place_cube("B", int(input("An welcher X Stelle?\n> ")) )
	print("B placed @ ", p_B)
	pp()
	print("\n")
	
	time.sleep(time2wait)
	
	if check_win("B"):
		playing = False
		continue
	
	time.sleep(time2wait)
	
	
	p_A = place_cube("A", make_move("A"))
	poss_moves(p_A[0], p_A[1])
	
	moves = shuffle()
	
	print("A placed @ ", p_A)
	pm()
	pp()
	print("\n")
	
	time.sleep(time2wait)
	
	if check_win("A"):
		playing = False
		continue
	
	print(" ########### END ROUND ########### ")
	
	time.sleep(time2wait)
	
	gameround += 1
	
	print("\n\n")

pp()