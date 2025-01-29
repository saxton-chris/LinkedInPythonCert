from typing import List, Tuple, Optional

def find_empty_cell(grid: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Finds the first empty cell (value 0) in the Sudoku grid.

    Args:
        grid (List[List[int]]): A 9x9 list representing the Sudoku puzzle.

    Returns:
        Optional[Tuple[int, int]]: The row and column index of the first empty cell, or None if all cells are filled.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(grid: List[List[int]], row: int, col: int, num: int,
             rows: List[set], cols: List[set], blocks: List[set]) -> bool:
    """
    Checks if placing a number in a specified cell is valid using precomputed sets.

    Args:
        grid (List[List[int]]): A 9x9 list representing the Sudoku puzzle.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to check.
        rows (List[set]): A list of sets representing numbers used in each row.
        cols (List[set]): A list of sets representing numbers used in each column.
        blocks (List[set]): A list of sets representing numbers used in each 3x3 block.

    Returns:
        bool: True if the number can be placed in the cell, False otherwise.
    """
    block_index = (row // 3) * 3 + (col // 3)
    return num not in rows[row] and num not in cols[col] and num not in blocks[block_index]

def solve_sudoku(puzzle: List[List[int]]) -> bool:
    """
    Solves a given Sudoku puzzle using optimized backtracking.

    Args:
        puzzle (List[List[int]]): A 9x9 list representing the Sudoku puzzle.

    Returns:
        bool: True if the puzzle is solvable and solved in-place, False otherwise.

    Raises:
        Exception: If the puzzle is not a 9x9 grid or contains invalid values.
    """
    # Validate input
    if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
        raise Exception("Puzzle must be a 9x9 grid")
    if any(num < 0 or num > 9 or not isinstance(num, int) for row in puzzle for num in row):
        raise Exception("All values must be integers between 0 and 9")

    # Initialize sets to track used numbers in rows, columns, and 3x3 blocks
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]

    # Prepopulate sets with existing numbers
    for r in range(9):
        for c in range(9):
            num = puzzle[r][c]
            if num != 0:
                rows[r].add(num)
                cols[c].add(num)
                blocks[(r // 3) * 3 + (c // 3)].add(num)

    def backtrack() -> bool:
        # Find the next empty cell
        empty_cell = find_empty_cell(puzzle)
        if not empty_cell:
            return True

        row, col = empty_cell
        block_index = (row // 3) * 3 + (col // 3)

        # Try placing numbers 1-9
        for num in range(1, 10):
            if is_valid(puzzle, row, col, num, rows, cols, blocks):
                # Place the number
                puzzle[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                blocks[block_index].add(num)

                # Recurse to solve the rest of the puzzle
                if backtrack():
                    return True

                # Undo the move if it leads to no solution
                puzzle[row][col] = 0
                rows[row].remove(num)
                cols[col].remove(num)
                blocks[block_index].remove(num)

        return False

    return backtrack()

def print_sudoku(sudoku: List[List[int]]) -> None:
    """
    Prints a Sudoku puzzle in a readable grid format.

    Args:
        sudoku (List[List[int]]): A 9x9 list representing the Sudoku puzzle.
    """
    for row in range(9):
        row_string = ''
        for col in range(9):
            if sudoku[row][col] == 0:
                row_string += ' . '
            else:
                row_string += f' {sudoku[row][col]} '
            if col in {2, 5}:
                row_string += '|'
        print(row_string)
        if row in {2, 5}:
            print('-' * 21)

if __name__ == '__main__':
    # Example Sudoku puzzle with some cells pre-filled (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("The original puzzle is:")
    print_sudoku(puzzle)

    # Solve the Sudoku puzzle
    if solve_sudoku(puzzle):
        print("The puzzle was solved!")
        print_sudoku(puzzle)
    else:
        print("The puzzle has no solution.")
