def safe(board,row,col,n):
    for i in range(col):
        if board[[row][i]] == 1:
            return False
    
    while row >=0 and col >= 0:
        if board[[row][col]] == 1:
            return False
        row += 1
        col -= 1

    while row < n and col >= 0:
        if board[[row][col]] == 1:
            return False
        row += 1
        col -= 1
    
    
def n_queens(board,col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if safe(board, i, col, n):
            board[i][col] = 1
            if n_queens(board, col+1, n):
                return True
            board[i][col] = 0
    return False

def main():
    board = [[0] * n for _ in range(n)]
    pass    

n = 8
if __name__ == "__main__":
    main()