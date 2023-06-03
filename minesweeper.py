# Compulsory Task 1
# Create a file named minesweeper.py
# Create a function that takes a grid of # and -, where each hash (#) represents a
# mine and each dash (-) represents a mine-free spot.
# Return a grid, where each dash is replaced by a digit, indicating the number of
# mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).

# First define the minesweeper function
def minesweeper(grid):
    # Get the size of input grid
    rows = len(grid)
    cols = len(grid[0])
    # Use nested for loop to get the current position and value of the grid
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "-":
                count = 0
                # Let the variables i,j represent adjacent cells of current position r,c and iterate all to check if there is mine
                for i, j in [
                    (r-1, c-1), (r-1, c), (r-1, c+1),
                    (r, c-1),             (r, c+1),
                    (r+1, c-1), (r+1, c), (r+1, c+1),
                ]:
                    # If mines are found in adjacent cells count value will +1
                    if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "#":
                        count += 1
                # Replace the cells which are not mine with the count value to give hints on the mine location
                grid[r][c] = str(count)


    return grid

# Create a grid and call out the minesweeper function to show the location of mines and all the hints
grid = [
["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]
]

# Print out the input grid
print("This is the input grid.")
for input_row in grid:
    str_input__row = str(input_row)
    print(input_row)

# Print out the output of minesweeper
print("Here is the output of the minesweeper.")
result = minesweeper(grid)
for new_row in result:
    str_row = str(new_row)
    print(str_row)



