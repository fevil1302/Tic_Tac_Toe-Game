import itertools

game=[ [0,0,0],
		[0,0,0],
		[0,0,0]]
def win_game(current_game):
	#Horizontal
	for row in current_game:
		if row.count(row[0])==len(row) and row[0] !=0:
			print(f" \n Player {current_player} Winner!!! horizontally(--) \n")
			return True

	#Diagonal
	diags=[]
	for col,row in enumerate(reversed(range(len(current_game)))):
		diags.append(current_game[row][col])
	if diags.count(diags[0])==len(diags) and diags[0] !=0:
		print(f"\n Player {current_player} Winner!!! diagonally(/) \n")	
		return True

	diags=[]
	for ix in range(len(current_game)):
		diags.append(current_game[ix][ix])
	if diags.count(diags[0])==len(diags) and diags[0] !=0:
		print(f" \n Player {current_player} Winner!!! diagonally(\\) \n")	
		return True

	#Vertical
	for col in range(len(current_game)):
		check=[]
		for row in current_game:
			check.append(row[col])
	if check.count(check[0])==len(check) and check[0] !=0:
		print(f" \n Player {current_player} Winner!!! vertically(|) \n")	
		return True
	return False


def game_board(game_map,player=0,row=0,column=0,just_display=False):
	try:
		if game_map[row][column] != 0:
			print("\this position already occupied!!! \\n")
			return game_map,False
		print("   a  b  c")
		if not just_display:
			game_map[row][column]= player
		for count,row in enumerate(game_map):
			print(count,row)
		return game_map,True 
	except IndexError as e:
		print("ERROR: input row/column between 0 to 2",e)
		return game_map,False
	except Exception as e:
		print("Something went wrong",e)
		return game_map,False	


play=True
players=[1,2]
while play:
	game=[ [0,0,0],
		  [0,0,0],
		  [0,0,0]]

	game_won=False
	game,_=game_board(game,just_display=True)
	player_choice = itertools.cycle([1,2])
	while not game_won:
		current_player=next(player_choice)
		print(f"Current Player:{current_player}")
		played=False

		while not played:
			row_choice = int(input("Enter Position of Row :"))
			column_choice = int(input("Enter Position of Column:"))
			game,played=game_board(game,current_player,row_choice,column_choice)
		
		if win_game(game):
			game_won = True
			again = input("Would you like to play AGAIN (y/n)")
			if again.lower()=="y":
				print("Restarting...")
			elif again.lower()=="n":
				print("Byeee.")
				play=False
			else:
				print("Not a Valid answer!! Byeee")
				play=False
				
				