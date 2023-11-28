sudoku = [
    [9,0,8,0,0,4,1,6,2],
    [3,1,2,6,8,5,4,7,9],
    [6,7,4,2,1,9,5,3,8],
    [7,8,1,9,2,6,3,4,5],
    [4,3,9,8,5,1,7,2,6],
    [0,2,0,0,7,3,8,9,0],
    [8,6,3,0,9,7,0,5,0],
    [0,9,5,0,4,2,0,0,0],
    [0,0,0,0,0,0,9,0,0]
]

def solve_sudoku(sudoku):
    if is_complete(sudoku) == True and is_valid(sudoku) == True:
        return sudoku
    
    else:
        for row in enumerate(sudoku):
            for column in enumerate(row[1]):
                if column[1] == 0:
                    column_0 = column[0]
                    break
            if row[1][column[0]] == 0:
                row_0 = row[0]
                break
        
        while (sudoku[row_0][column_0] < 9):
            sudoku[row_0][column_0] += 1
            if is_valid(sudoku) == False:
                continue
            next_sudoku = solve_sudoku(sudoku)
            if next_sudoku == "NO SOLUTION":
                continue
            else:
                return next_sudoku
        else:
            return "NO SOLUTION"
            
def is_valid(sudoku):
    for row in sudoku:
        if is_valid_group(row) == False:
            return False
    
    for column in range(0,9):
        column_list = []
        for row in range(0,9):
            column_list.append(sudoku[row][column])
        if is_valid_group(column_list) == False:
            return False
    
    for upper_corner_row in range(0, 9, 3):
        for upper_corner_column in range(0, 9, 3):
            grid_list = []
            for i in range(0,3):
                for j in range(0,3):
                    grid_list.append(sudoku[upper_corner_row + i][upper_corner_column + j])
            if is_valid_group(grid_list) == False:
                return False

    return True

def is_valid_group(group):
    seen = []
    for entry in group:
        if entry in seen:
            return False
        if entry != 0:
            seen.append(entry)
    return True

def is_complete(sudoku):
    for row in enumerate(sudoku):
        for column in enumerate(row[1]):
            if sudoku[row[0]][column[0]] == 0:
                return False

    return True

print(solve_sudoku(sudoku))
