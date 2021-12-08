# 0, 1, 2
# 3, 4, 5
# 6, 7, 8
board = [2, 1, 0,
         2, 1, 0,
         2, 1, 0]

for i in range(len(board)):
    if board[i] == 0:
        print('#', end=' ')
    elif board[i] == 1:
        print('X', end=' ')
    elif board[i] == 2:
        print('O', end=' ')

    if (i + 1) % 3 == 0:
        print()
print()


def check_win():
    for i in range(len(board)):
        # Checks columns
        if i <= 2:
            if board[i] == board[i + 3] == board[i + 6]:
                print('Player', board[i], 'Won!')
                return
        # Checks rows
        if i % 3 == 0:
            if board[i] == board[i + 1] == board[i + 2]:
                print('Player', board[i], 'Won!')
                return
        # Checks negative diagonal
        if i == 0:
            if board[i] == board[i + 4] == board[i + 8]:
                print('Player', board[i], 'Won!')
                return
        # Checks positive diagonal
        if i == 2:
            if board[i] == board[i + 2] == board[i + 4]:
                print('Player', board[i], 'Won!')
                return


check_win()
