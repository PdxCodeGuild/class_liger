
# Lab 20: Adventure

Create a `Character` and `Enemy` class. 

Create a game board with a list of lists.

Randomly place enemies on the board.

Write a REPL that allows the character to move around the board until they encounter an enemy, then battle the enemy until one of the characters is defeated.

If the character defeats all the enemies, they win. Otherwise, they lose.
# Create a board with the given width and height
```
width = 10  # the width of the board
height = 10  # the height of the board
```
# Use a list of lists to represent the board
```
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board        
```

# Define the player position
```
player.i = 4
player.j = 4
```

# Add 4 enemies in random locations
```
for i in range(4):
    enemy.i = random.randint(0, height - 1)
    enemy.j = random.randint(0, width - 1)
    board[enemy.i][enemy.j] = '§'
```

# Loop until the user says 'done' or is defeated
```
while True:
    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player.j -= 1  # move left
    elif command == 'right':
        player.j += 1  # move right
    elif command == 'up':
        player.i -= 1  # move up
    elif command == 'down':
        player.i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player.i][player.j] == '§':
        print('You\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('You\'ve slain the enemy')
            board[player.i][player.j] = ' '  # remove the enemy from the board
        else:
            print('You hestitated and were slain')
            break

            # print out the board

    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player.i and j == player.j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
```