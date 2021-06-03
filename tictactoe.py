#Alex Lewis

#Gameboard exampple
print("this is the asigned gameboard keymap")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")


  
global name1
global name2
name1 = input("First player as X:  ")
name2 = input("Second player as O (For singleplayer enter BOT: ") 
if name2 == 'BOT':
  bots()


# Gameboard
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
 
# Variables

    
  

game_going = True
winner = None
current_player = "X"

# Score of players
score_x = 0
score_o = 0
 
# Print board
def display_board():
  print(board[0] + " | " + board[1] + " | " +board[2])
  print(board[3] + " | " + board[4] + " | " +board[5])
  print(board[6] + " | " + board[7] + " | " +board[8])
 
# Recall
def play_game():
  global score_x, score_o
 
  display_board()
 
  while game_going:
    handle_turn(current_player)
 
    check_gameover()
 
    flip_turns()
 
  if winner == "X":
    score_x += 1
    print(name1, "won!")
  if winner == "O":
    score_o += 1
    print(name2, "won!")
  elif winner == None:
    # No one gains points
    print("Tie!")
 
# Turns
def handle_turn(player):
 
  print(player + "'s turn.")
  position = input("Choose a position from 1-9:")
 
  valid = False
  while not valid:
 
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input, choose a position from 1-9:")
 
    position = int(position) - 1
 
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
 
 
  board[position] = player
 
  display_board()
 
 
# Checkgame
def check_gameover():
  check_win()
  check_tie()
 
 
 
# Check win
def check_win():
 
  global winner
 
 
  # Check for rows, columns, or diagonals
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return
 
def check_rows():
  global game_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
 
  if row_1 or row_2 or row_3:
    game_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return
 
def check_columns():
  global game_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
 
  if column_1 or column_2 or column_3:
    game_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return
 
def check_diagonals():
  global game_going
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[2] == board[4] == board[6] != "-"
 
 
  if diagonals_1 or diagonals_2:
    game_going = False
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return
 
# Check tie
def check_tie():
  global game_going
  if "-" not in board:
    game_going = False
  return
 
def flip_turns():
  global current_player
  if current_player == "X":
    current_player= "O"
  elif current_player == "O":
    current_player = "X"
  return

# Play again
while True:
  play_game()
  
  # Print score after game end
  print(name1, "gained " + str(score_o) + " points")
  print(name2, "gained " + str(score_x) + " points")
  
  # TODO: Add support for "no", "N" and so on
  if input("Play again (y/n): ") == "n":
    break;

  # Reset gameboard
  board = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
 
  # Variables too
  game_going = True
  winner = None
  current_player = "X"

  # Reset scores
  # TODO: Add support for "yes", "Y"
  if input("Reset score (y/n): ") == "y":
    score_x = 0
    score_y = 0

