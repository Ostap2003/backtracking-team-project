
from pprint import pprint
import pygame
import time

'''The module has class Grid for solving sudoku.
Grid should be given as a list of integers or a path to a file.
'''

pygame.init()
screen = pygame.display.set_mode((459, 459))

class Grid():
    '''Class for solving sudoku.
    '''
    def __init__(self, path= None, grid= None) -> None:
        '''Initialize grid, columns, squares.
        '''
        self.grid = []
        if grid:
            assert type(grid) == list
            self.grid = grid
        elif path:
            grid = self.read_and_convert_to_grid(path)
        self.check_grid_accuracy()
        self.columns = []
        self.squares = []
        self.expand_data()

    def show_sudoku(self):
        '''Displays current grid (self.grid).
        '''
        x, y = 0, 0
        for line in self.grid:
            for num in line:
                pygame.draw.rect(screen, 'green', pygame.Rect(x, y, 50, 50))
                font = pygame.font.SysFont(None, 40)
                img = font.render(str(num), True, 'black')
                screen.blit(img, (x + 19, y + 12))
                x += 51
                if x == 153 or x == 308:
                    x += 2
                pygame.display.update()
            y += 51
            if y == 153 or y == 308:
                y += 2
            x = 0

    def read_and_convert_to_grid(self, path):
        '''Reads from file and writes info to list grid.
        '''
        with open(path, 'r') as file:
            for line in file:
                if line[-1] == '\n':
                    line = line[:-1]
                self.grid.append([int(item) for item in line])
            print(self.grid)

    def write_to_file(self):
        '''Writes solved sudoku to file 'solved_sudoku.txt'.
        '''
        with open('solved_sudoku.txt', 'w') as file:
            to_write = ''
            for row in self.grid:
                row = [str(i) for i in row]
                to_write += ''.join(row) + '\n'
            file.write(to_write[:-1])

    def expand_data(self):
        '''Fills lists self.columns and self.squares.
        '''

        for i in range(9):
            col = []
            for j in range(9):
                col.append(self.grid[j][i])
            self.columns.append(col)


        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for x in range(3):
                        square.append(self.grid[i*3 + k][j*3 + x])
                self.squares.append(square)

        


    def check_grid_accuracy(self):
        '''Checks if grid content is appropriate.
        '''

        for i in range(9):
            for j in range(9):
                assert 0 <= self.grid[i][j] <= 9
            return True



    def solve_sudoku(self, row, col):
        '''Recursion, which solves sudoku.
        '''

        self.show_sudoku()
        time.sleep(0.0001)

        union = set(self.squares[col//3 + (row//3)*3]).union(set(self.grid[row]))
        union = union.union(self.columns[col])

        if col == 8:
            next_col = 0
            next_row = row + 1
        else:
            next_col = col + 1
            next_row = row

        if self.grid[row][col] != 0:
            if next_row == 9:

                return True
            return self.solve_sudoku(next_row, next_col)
        for i in range(1, 10):
            if i not in union:
                self.grid[row][col] = i
                self.columns[col][row] = i
                self.squares[col//3 + (row//3)*3][(row % 3)*3 + (col % 3)] = i
                if next_row == 9:
                    self.show_sudoku()
                    return True
                if self.solve_sudoku(next_row, next_col):
                    return True
        self.grid[row][col] = 0
        self.columns[col][row] = 0
        self.squares[col//3 + (row//3)*3][(row % 3)*3 + (col % 3)] = 0
        return False


# grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
#          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
#          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
#          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
#          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
#          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
#          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
#          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
#          [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

# sudoku = Grid('grid_2.txt')
# sudoku.solve_sudoku(0, 0)
# sudoku.write_to_file()
# time.sleep(5)