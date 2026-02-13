# 2019 SH2 CT Practical - Question 4

# Task 4.1
class MagicSquare():
    
    def __init__(self, n):
        self.n = n
        self.grid = []
        current = 1
        for i in range(n):
            self.grid.append([])
            for j in range(n):
                self.grid[i].append(current)
                current += 1
                
    def print(self):
        width = len(str(self.n**2))
        line = "-" * ((width + 2) * self.n + self.n + 1)
        print(line)
        for i in range(len(self.grid)):
            current = "|"
            for j in range(len(self.grid[i])):
                value = str(self.grid[i][j])
                current += " " + "0" * (width - len(value))
                current += str(self.grid[i][j]) + " |"
            print(current)
            print(line)



# Task 4.2
class MagicSquare():
    
    def __init__(self, n):
        self.n = n
        self.grid = []
        current = 1
        for i in range(n):
            self.grid.append([])
            for j in range(n):
                self.grid[i].append(current)
                current += 1
                
    def swap(self, rowA, colA, rowB, colB):
        self.grid[rowA][colA] = self.grid[rowB][colB]
        
    def print(self):
        width = len(str(self.n**2))
        line = "-" * ((width + 2) * self.n + self.n + 1)
        print(line)
        for i in range(len(self.grid)):
            current = "|"
            for j in range(len(self.grid[i])):
                value = str(self.grid[i][j])
                current += " " + "0" * (width - len(value))
                current += str(self.grid[i][j]) + " |"
            print(current)
            print(line)



# Task 4.3
class MagicSquare():
    
    def __init__(self, n):
        self.n = n
        self.grid = []
        current = 1
        for i in range(n):
            self.grid.append([])
            for j in range(n):
                self.grid[i].append(current)
                current += 1
                
    def swap(self, rowA, colA, rowB, colB): # 0-indexed
        self.grid[rowA][colA] = self.grid[rowB][colB]

    def solved(self):
        # required sum
        seqSum = ((self.n**2 * (self.n**2 + 1)) / 2) / self.n

        # row sums
        rowSums = []
        for row in range(len(self.grid)):
            rowSum = 0
            for col in range(len(self.grid[row])):
                rowSum += self.grid[row][col]
            rowSums.append(rowSum)
                
        # col sums
        colSums = []
        for col in range(self.n): # each col
            colSum = 0
            for row in range(self.n): # each row
                colSum += self.grid[row][col]
            colSums.append(colSum)
        
        # diagonals - given square matrix
        diaSums = [0, 0] # pri & sec diag sums respectively
        for i in range(self.n):
            diaSums[0] += self.grid[i][i]
            diaSums[1] += self.grid[i][self.n - i - 1]

        allSeq = rowSums + colSums + diaSums
        for i in range(len(allSeq)):
            if allSeq[i] != seqSum:
                return False
        return True

    def print(self):
        width = len(str(self.n**2))
        line = "-" * ((width + 2) * self.n + self.n + 1)
        print(line)
        for i in range(len(self.grid)):
            current = "|"
            for j in range(len(self.grid[i])):
                value = str(self.grid[i][j])
                current += " " + "0" * (width - len(value))
                current += str(self.grid[i][j]) + " |"
            print(current)
            print(line)



# Task 4.4
class MagicSquare():
    
    def __init__(self, n):
        self.n = n
        self.grid = []
        current = 1
        for i in range(n):
            self.grid.append([])
            for j in range(n):
                self.grid[i].append(current)
                current += 1
                
    def swap(self, rowA, colA, rowB, colB): # 0-indexed
        temp = self.grid[rowA][colA]
        self.grid[rowA][colA] = self.grid[rowB][colB]
        self.grid[rowB][colB] = temp

    def solved(self):
        # required sum
        seqSum = ((self.n**2 * (self.n**2 + 1)) / 2) / self.n

        # row sums
        rowSums = []
        for row in range(len(self.grid)):
            rowSum = 0
            for col in range(len(self.grid[row])):
                rowSum += self.grid[row][col]
            rowSums.append(rowSum)
                
        # col sums
        colSums = []
        for col in range(self.n): # each col
            colSum = 0
            for row in range(self.n): # each row
                colSum += self.grid[row][col]
            colSums.append(colSum)
        
        # diagonals - given square matrix
        diaSums = [0, 0] # pri & sec diag sums respectively
        for i in range(self.n):
            diaSums[0] += self.grid[i][i]
            diaSums[1] += self.grid[i][self.n - i - 1]

        allSeq = rowSums + colSums + diaSums
        for i in range(len(allSeq)):
            if allSeq[i] != seqSum:
                return False
        return True

    def print(self):
        width = len(str(self.n**2))
        line = "-" * ((width + 2) * self.n + self.n + 1)
        print(line)
        for i in range(len(self.grid)):
            current = "|"
            for j in range(len(self.grid[i])):
                value = str(self.grid[i][j])
                current += " " + "0" * (width - len(value))
                current += str(self.grid[i][j]) + " |"
            print(current)
            print(line)

    def findCell(self, v):
        #print("current v: " + str(v))
        if v > self.n**2:
            raise ValueError
        else:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    #print("\tchecking: (" + str(i) + "," + str(j) + \
                          #"): " + str(self.grid[i][j]))
                    if self.grid[i][j] == v:
                        #print("\t\tFOUND!")
                        return (i, j)

# initialise the magic square
import random
#n = random.randint(5, 10)
n = 3
ms = MagicSquare(n)

# guess and check method to find a solution
# assume guess = [R1C1, R1C2, R1C3, ..., R2C1, R2C2, R2C3, ...]
numbers = [i for i in range(1, n**2 + 1)]
while not ms.solved():
    random.shuffle(numbers) # shuffle elements in place
    for row in range(n):
        for col in range(n):
            pos = ms.findCell(numbers[(row * n) + col])
            ms.swap(row, col, pos[0], pos[1])
ms.print()
print("Solved? " + str(ms.solved()))
