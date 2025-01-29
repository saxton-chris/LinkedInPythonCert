from typing import List, Tuple

def find_empty_cell(grid: List[List]) -> (Tuple[int, int]):
    """
    Finds the first empty cell in the Sudoku grid.

    Args:
        grid (List[List]): A 9x9 list representing the Sudoku puzzle.

    Returns:
        Tuple[int, int]: The row and column index of the first empty cell (value 0),
        or None if all cells are filled.
    """
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid(grid: List[List], row: int, col: int, num: int) -> bool:
    """
    Checks if placing a number in a specified cell is valid according to Sudoku rules.

    Args:
        grid (List[List]): A 9x9 list representing the Sudoku puzzle.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to check.

    Returns:
        bool: True if the number can be placed in the cell, False otherwise.
    """
    # Check the row
    for c in range(0, 9):
        if grid[row][c] == num:
            return False
        
    # Check the column
    for r in range(0, 9):
        if grid[r][col] == num:
            return False
        
    # Check the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def solve_sudoku(puzzle: List[List]) -> bool:
    """
    Solves a given Sudoku puzzle using backtracking.

    Args:
        puzzle (List[List]): A 9x9 list representing the Sudoku puzzle.

    Returns:
        bool: True if the puzzle is solvable and solved in-place, False otherwise.

    Raises:
        Exception: If the puzzle is not a 9x9 grid or contains invalid values.
    """
    # Ensure the puzzle is a valid 9x9 grid
    if len(puzzle) != 9:
        raise Exception("Puzzle must have 9 rows")
    
    for row in puzzle:
        if len(row) != 9:
            raise Exception("Puzzle must have 9 columns")
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                raise Exception("All values must be an integer 0-9")

    # Find the first empty cell
    empty_cell = find_empty_cell(puzzle)

    # If no empty cells, the puzzle is solved
    if empty_cell is None:
        return True
    
    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num  # Place the number

            # Recursively attempt to solve the rest of the puzzle
            if solve_sudoku(puzzle):
                return True
            
            # If placing the number didn't lead to a solution, reset the cell
            puzzle[row][col] = 0

    return False

def print_sudoku(sudoku: List[List]) -> None:
    """
    Prints a Sudoku puzzle in a readable grid format.

    Args:
        sudoku (List[List]): A 9x9 list representing the Sudoku puzzle.
    """
    for row in range(0, 9):
        row_string = ''
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                row_string += f' * '
            else:
                row_string += f' {sudoku[row][col]} '
            if col == 2 or col == 5:
                row_string += ' | '
        if row == 2 or row == 5:
            print('---------------------------------')
        print(row_string)

if __name__ == '__main__':
    # Example Sudoku puzzle with some cells pre-filled (0 represents empty cells)
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
    print_sudoku(puzzle)

    # Solve the Sudoku puzzle
    solved = solve_sudoku(puzzle)

    if solved:
        print("The puzzle was solved!")
        print_sudoku(puzzle)
    else:
        print("Puzzle has no solution")
