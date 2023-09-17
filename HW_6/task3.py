def n_queens(board,col, N)



def safe(board,row,col,N):
    for i in range(col):
        if board[[row][i]] == 1:
            return False
    
    while row >=0 and col >= 0:
        if board[[row][col]] == 1:
            return False
        row += 1
        col -= 1
    
