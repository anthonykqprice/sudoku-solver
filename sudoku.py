sudoku = [
    [0,0,8,0,0,0,4,0,0],
    [0,5,0,3,0,0,7,0,1],
    [3,0,0,0,0,2,0,0,0],
    [0,0,0,1,0,0,0,4,0],
    [0,6,0,0,0,0,0,2,0],
    [0,0,7,0,0,9,1,0,6],
    [0,0,9,0,8,0,0,0,0],
    [0,7,0,2,0,0,3,0,5],
    [0,0,0,0,0,0,0,6,0]
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
            sudoku[row_0][column_0] = 0
            return "NO SOLUTION"
            
def is_valid(sudoku):
    for row in sudoku:
        if is_valid_group(row) == False:
            #print(f'row invalid at {row}')
            return False
    
    for column in range(0,9):
        column_list = []
        for row in range(0,9):
            column_list.append(sudoku[row][column])
        if is_valid_group(column_list) == False:
            #print(f'column invalid at {column}')
            return False
    
    for upper_corner_row in range(0, 9, 3):
        for upper_corner_column in range(0, 9, 3):
            grid_list = []
            for i in range(0,3):
                for j in range(0,3):
                    grid_list.append(sudoku[upper_corner_row + i][upper_corner_column + j])
            if is_valid_group(grid_list) == False:
                #print(f'grid invalid at {row} {column}')
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

def print_sudoku(sudoku):
    if sudoku == 'NO SOLUTION':
        print(sudoku)
    else:
        for row in sudoku:
            print(row)

print_sudoku(solve_sudoku(sudoku))


