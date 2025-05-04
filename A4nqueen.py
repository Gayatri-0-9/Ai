def is_safe(board,row,col,n):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,n),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def util(board,col,n):
    if col>=n:
        return True
    for row in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            if util(board,col+1,n):
                return True
        board[row][col]=0
    return False
def solve(n):
    board=[[0]*n for _ in range (n)]
    if util(board,0,n):
        return board
    else:
        return None
def print_board(board):
    for row in board:
        print(' '.join('Q' if cell==1 else '.' for cell in row))
n=int(input('Enter n:'))
solution=solve(n)
if solution:
    print(f'Solution for {n}-queens is:')
    print_board(solution)
else:
    print(f'No solution for {n}-queens!')