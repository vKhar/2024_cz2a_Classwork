class TicTacToe:
    def __init__(self,n):
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.size = n
        self.moveLeft=n*n
    def make_move(self,player,row,col):
        if self.board[row][col] == None:
            self.board[row][col] = player
            self.moveLeft-=1
            return True
        else:
            print("Invalid Move")
            return False
    def print(self):
        for r in self.board:
            r=map( lambda x: "X" if x is None else x ,r)
            print(" ".join([ f"{c:^2}" for c in r]))
        print()              
    def _check_win(self):
        def check_vertical(player):
            for col in range(self.size):
                for row in range(self.size):
                    if self.board[row][col] != player:
                        break
                else:
                    return True
            return False
        def check_horizontal(player):
            for row in self.board:
                if row == [player]*self.size:
                    return True
            return False
        def check_diagonal(player):
            for i in range(self.size):
                if self.board[i][i] != player:
                    break
            else:
                return True
            for i in range(0,self.size):
                if self.board[i][self.size-1-i] != player:
                    return False
            else:
                return True        
        for player in (0,1):
            # print("v",check_vertical(player))
            # print("h",check_horizontal(player))
            # print("d",check_diagonal(player))
            if check_horizontal(player) or \
                check_vertical(player) or \
                    check_diagonal(player):
                    print(f"Player:{player} wins")
                    return True
        else:
            if self.moveLeft == 0:
                print("Draw")
                return True
            else:
                return False


p=TicTacToe(3)
player=0
while not p._check_win():
    p.print()
    move=input(f"Enter player {player} move:")
    x,y = [ int(c) for c in move.split(",")]
    if p.make_move(player,x,y):
        p.print()
        player=(player+1)%2

