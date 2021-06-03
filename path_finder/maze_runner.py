import turtle
from stack import Stack
from pprint import pprint

class PathFinder:
    """Find path in a maze"""
    PATH = "o"
    WALL = "*"
    USED = "-"

    def __init__(self, start: tuple, finish: tuple, maze=None, path=None, draw_maze=False):
        self.start_pos = start
        self.exit = finish
        self.draw_maze = draw_maze
        
        if maze:
            self.maze = maze
            self.maze_rows = len(maze)
            self.maze_cols = (len(maze[0]))
        else:
            self.maze_rows = 0
            self.maze_cols = 0
            self.maze = self.read_maze(path)
        
        if self.draw_maze:
            self.my_pen = turtle.Turtle()
            self.my_pen._tracer(0)
            self.my_pen.speed(1)
            self.my_pen.hideturtle()


    def read_maze(self, path):
        """Reads file with maze, and trasforms it into a list of lists"""
        maze = []
        with open(path, 'r', encoding='utf-8') as maze_fl:
            for line in maze_fl:
                self.maze_rows += 1
                line = line.strip()
                row = []
                for el in line:
                    row.append(el)
                maze.append(row)

        self.maze_cols = len(maze[0])
        return maze

    def find_path(self):
        """Find a route that connects entrance to the maze
        with the exit, if there is exit.
        Makes moves in the following order:
        up, right, left, down"""
        moves_stack = Stack()
        current_pos = self.start_pos
        moves_stack.add(current_pos)
        self.set_cell(current_pos, self.PATH)
        possible_routes = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        while (not self._exit_found(current_pos)):
            next_move_found = False
            for move in possible_routes:
                if self._valid_move(current_pos, move):
                    current_pos = current_pos[0] + move[0], current_pos[1] + move[1]
                    self.set_cell(current_pos, self.PATH)
                    moves_stack.add(current_pos)
                    next_move_found = True

                    # draw here a cell with turtle
                    if self.draw_maze:
                        self.my_pen.clear()
                        self.build_maze()
                        self.my_pen.getscreen().update()
                    break

            if not next_move_found:
                moves_stack.pop_el_from_stack()
                self.set_cell(current_pos, self.USED)

                # mark curr cell with grey col
                if self.draw_maze:
                        self.my_pen.clear()
                        self.build_maze()
                        self.my_pen.getscreen().update()
                current_pos = moves_stack.peek()
        
        if self.draw_maze:
            self.my_pen.getscreen().update()
            turtle.done()

    def _exit_found(self, current_pos):
        """Check if current position equals to the exit position"""
        return self.exit == current_pos

    def _valid_move(self, current_pos, move):
        """Check if move is valid"""
        possible_mv = current_pos[0] + move[0], current_pos[1] + move[1]

        # check if possible move is in board range
        if possible_mv[0] in range(0, self.maze_rows) and\
            possible_mv[1] in range(0, self.maze_cols):

            cell_val = self.get_cell(possible_mv)
            if cell_val == " ":
                return True

        return False
    
    def get_cell(self, position):
        """Return value that belongs to the cell"""
        return self.maze[position[0]][position[1]]
    
    def set_cell(self, position: tuple, value: str):
        """Set a value for cell on the given position"""
        self.maze[position[0]][position[1]] = value

    def __str__(self):
        """String representation of the maze"""
        maze = ""
        for row in self.maze:
            for el in row:
                maze += el
            maze += "\n"
        return maze.strip()

    def box(self, side):
        """Builds a box, an element of the maze that can be a wall, path, or unvisited cell"""
        self.my_pen.begin_fill()
        for _ in range(3):
            self.my_pen.forward(side)
            self.my_pen.left(90)

        self.my_pen.forward(side)
        self.my_pen.end_fill()
        self.my_pen.setheading(0)

    def build_maze(self):
        """Builds a whole maze using box func as a helper"""
        side = 30
        self.my_pen.penup()
        self.my_pen.goto(-130,130)
        self.my_pen.setheading(0)
        for row in self.maze:
            for col in row:
                if col == "*":
                    self.my_pen.color("#000000")
                elif col == "o":
                    self.my_pen.color("#4fff98")
                elif col == "-":
                    self.my_pen.color("#ff7e4f")
                else:
                    self.my_pen.color("#FFFFFF")
                self.box(side)
                self.my_pen.penup()
                self.my_pen.forward(side)
                self.my_pen.pendown()

            self.my_pen.penup()
            self.my_pen.setheading(270)
            self.my_pen.forward(side)
            self.my_pen.setheading(180)
            self.my_pen.forward(side * self.maze_cols)
            self.my_pen.setheading(0)
            self.my_pen.pendown()


if __name__ == '__main__':
    p = PathFinder((4, 1), (4, 3), path="path_finder/mazes/maze.txt", draw_maze=True)
    p = PathFinder((0,1), (11, 7), path="path_finder/mazes/maze2.txt", draw_maze=True)
    p = PathFinder((0, 1), (15, 14), path="path_finder/mazes/maze3.txt", draw_maze=True)

    p.find_path()
    print(p)
