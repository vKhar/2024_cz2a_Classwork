## 2019 NJC Prelim Paper 1
class HexBoard:
    def __init__(self,n):
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.size = n
        

    def print(self):
        for r in self.board:
            r=map( lambda x: "-" if x is None else x ,r)
            print(" ".join([ f"{c:^2}" for c in r]))
        print()

    def playX(self, row, col):
        return self._play("X", row, col)
    def playO(self, row, col):
        return self._play("O", row, col)    
    
    def _play(self, player, row, col):
        if self.board[row][col] is None:
            self.board[row][col]=player
            return True
        else:
            return False

    def _next(self, row, col):
        check=[]
        if row -1 > -1:
            check.append ((row-1,col))
        if row-1 > -1 and col+1 < self.size:
            check.append((row-1,col+1))
        if col -1 > -1:
            check.append((row,col-1))
        if col + 1 < self.size:
            check.append((row,col+1))
        if row+1 < self.size:
            check.append((row+1,col))
        if row+1 < self.size and col -1 > -1:
            check.append((row+1,col-1))
        return check

    def _win(self,cur, player):
        row, col = cur
        if player == "X"and col == self.size-1:
            return True
        if player == "O" and row == self.size-1:
            return True         
        check = self._next(row, col)
        self.board[row][col] = None
        for x, y in check:
            if self.board[x][y] == player:               
                if self._win((x,y), player):
                    return True
        return False

    def checkWinX(self):  
        board=[ [ c for c in r ] for r in self.board] 
        for row in range(self.size):
            if self.board[row][0] == "X":
                check = self._next(row,0)
                for x, y  in check:
                    if self.board[x][y] == "X":
                        self.board[row][0] = None   
                        if self._win((x,y),"X"):
                            return True
        self.board = board
        return False
    def checkWinO(self):
        board=[ [ c for c in r ] for r in self.board]        
        for col in range(self.size):
            if self.board[0][col] == "O":
                check = self._next(0,col)
                for x, y  in check:
                    if self.board[x][y] == "O":   
                        self.board[0][col] == None
                        if self._win((x,y), "O"):
                            return True
        self.board=board                
        return False

b=HexBoard(4)
# b.board = [ \
# [None,"O","O"],\
# ["X", "O", None],\
# ["O","X","X"]\
# ]
# b.print()
# print(
#  b.checkWinO()   
# )

p =("O","X")
player=0
b.print()
while True:
    move=input(f"Enter player {p[player]} move:")
    x,y = [ int(c) for c in move.split(",")]
    if b._play(p[player],x,y):
        b.print()
        if player == 0 and b.checkWinO():
            print("Player O Wins")
            break
        if player == 1 and b.checkWinX():
            print("Player X wins")
            break
        player=(player+1)%2

