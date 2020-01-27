'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
'''
'''#1'''
def numRookCaptures1(board):
    #find the position of R
    len_board = 8
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] == 'R':
                R_x, R_y = i, j

    #calculate the numbers captured by Rook
    counts = 0
    for i in range(R_y, -1, -1):
        if (board[R_x][i] == 'p'):
            counts += 1
            break
        elif board[R_x][i] == 'B':
            break

    for i in range(R_y+1, len_board):
        if (board[R_x][i] == 'p'):
            counts += 1
            break
        elif board[R_x][i] == 'B':
            break

    for i in range(R_x, -1, -1):
        if (board[i][R_y] == 'p'):
            counts += 1
            break
        elif (board[i][R_y] == 'B'):
            break

    for i in range(R_x+1, len_board):
        if (board[i][R_y] == 'p'):
            counts += 1
            break
        elif (board[i][R_y] == 'B'):
            break

    return counts

'''#2'''
def numRookCaptures2(board):
    #find the position of R
    len_board = 8
    for i in range(len_board):
        for j in range(len_board):
            if board[i][j] == 'R':
                R_x, R_y = i, j

    #calculate the numbers captured by Rook
    counts = 0
    counts += cal_num_at_x_direction(R_x, R_y, board)
    counts += cal_num_at_y_direction(R_x, R_y, board)

    return counts

def cal_num_at_x_direction(x, y, board):
    count = 0
    for i in range(y, -1, -1):
        if (board[x][i] == 'p'):
            count += 1
            break
        elif board[x][i] == 'B':
            break

    for i in range(y+1, 8):
        if (board[x][i] == 'p'):
            count += 1
            break
        elif board[x][i] == 'B':
            break
    return count

def cal_num_at_y_direction(x, y, board):
    count = 0
    for i in range(x, -1, -1):
        if (board[i][y] == 'p'):
            count += 1
            break
        elif (board[i][y] == 'B'):
            break

    for i in range(x+1, 8):
        if (board[i][y] == 'p'):
            count += 1
            break
        elif (board[i][y] == 'B'):
            break
    return count

#3
board =  [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
#0
board1 = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
#3
board2 = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(numRookCaptures2(board2))