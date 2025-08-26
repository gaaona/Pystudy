import sys

def checkBox(start_i, start_j, n): # 3*3 박스 안에 없는지 확인
    box_i = start_i//3 * 3
    box_j = start_j//3 * 3

    for k in range(3):
        for p in range(3):
            if sudoku[box_i+k][box_j+p] == n:
                return False
    
    return True


def checkRow(r, n): # 같은 행에 없는지 확인
    for c in range(9): # 
        if sudoku[r][c] == n: # 같은 숫자 있음
            return False
    
    return True

def checkCol(c, n): # 같은 열에 없는지 확인
    for r in range(9):
        if sudoku[r][c] == n: # 같은 숫자 있음
            return False
    
    return True


def dfs(idx):
    global blank

    if idx == len(blank):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        exit()

    br, bc = blank[idx]
    for i in range(1,10):
        if checkRow(br,i) and checkCol(bc,i) and checkBox(br,bc,i):
            sudoku[br][bc] = i
            dfs(idx+1)
            sudoku[br][bc] = 0


sudoku = []
blank = []

for i in range(9):
    line = list(map(int, sys.stdin.readline().rstrip()))
    for j in range(9):
        if line[j] == 0:
            blank.append((i, j))
    sudoku.append(line)

dfs(0)