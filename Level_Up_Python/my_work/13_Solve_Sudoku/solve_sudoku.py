from typing import List, Tuple

def find_empty_cell(grid: List[List]) -> Tuple:
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return (row, col)

    return None

def is_valid(grid, row, col, num) -> bool:
    for c in range(0, 9):
        if grid[row][c] == num:
            return False
        
    for r in range(0, 9):
        if grid[r][col] == num:
            return False
        
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def solve_sudoku(puzzle: List[List]) -> bool:
    if len(puzzle) != 9:
        raise Exception("Puzzle must have 9 rows")
    
    for row in puzzle:
        if len(row) != 9:
            raise Exception("Puzzle must have 9 columns")
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                raise Exception("All values must be an integer 0-9")

    empty_cell = find_empty_cell(puzzle)

    if empty_cell is None:
        return True
    
    row, col = empty_cell

    for num in range(1,10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return True
            
            puzzle[row][col] = 0


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print("The original puzzle is:")
    for row in puzzle:
        print(row)

    solved = solve_sudoku(puzzle)

    if solved:
        print("The puzzle was solved!")
        for row in puzzle:
            print(row)

    else:
        print("Puzzle has no solution")
