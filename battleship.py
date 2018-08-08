'''I had to fix it, it only showed the hit or "X "for the first turn.
So, it seemed logical that I had to move board[guess_row][guess_col] = "X"
right after the else and print, so on line 49. After I changed that that,
it showed the board with Xs for all the hits(well, missed, really).
But it didn't show any X if you got it right on the first try, so I
figured I had to copy board[guess_row][guess_col] = "X" and place it  a
fter the first if statement and "congratulations" part, but before the
break statement, otherwise the program would exit before reaching it.
And, lo and behold, it actually worked.
I tested it many times, and it still works. Pretty proud of myself for
understanding the issues and for debugging the program.
Oh, I also had to change len(board[0])-1
to len(board_in)-1, since len(board[0])-1 doesn't make much sense
(not sure why I wrote that), because it returns the same value as
len(board[2]) - 1, i.e. 0, and what we wanted is len(board) - 1,
so we wouldn't get a number that's out of range.
I also had to change a series of "board" parameters into "board_in"
parameters (really, they could've been called 'b' or anything else,
but it seemed to me that just calling them 'board' was a little bit
on the nose).
Furthermore, I had to wrap part of the code in a "try-except" block,
so that, if the user enters a value that's out of range, it doesn't stop
the program with an IndexError. Now that I handled the exception, the game
can just go on, although it exhausts one turn, so maybe I have to figure
something out that makes the program not take that turn into account,
if he enters a value that's out of range.'''

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

# print_board(board)

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) # For debugging purposes only, of course,
print(ship_col) # not for cheating :D

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    print("Turn", turn + 1)
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "X"
        break
    try:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            pass
            turn == 0
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
    except IndexError:
        print("Oops, that's not even in the ocean.")

if turn == 3:
    print("Game Over.")

print_board(board)
