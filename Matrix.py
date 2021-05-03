import numpy

class Matrix:
    def __init__(self, board, row, column, depth, way, previous):
        self.board = numpy.copy(board)
        self.row = row
        self.column = column
        self.result = numpy.array(self.generate_board())
        # zero_position[0] is a row number
        # zero_position[1] is a column number
        self.zero_position = self.find_zero_field()
        self.previous = previous
        self.way = way
        self.depth = depth

    # finding empty/zero position in the matrix
    def find_zero_field(self):
        zero = []
        #print("find_zero_field:")
        for i in range(len(self.board)):
            # print("i: ",i)
            for j in range(len(self.board[i])):
                # print('j: ', j)
                if self.board[i][j] == 0:
                    zero.append(i)
                    zero.append(j)
        # print("returned: ", zero)
        return zero

    # generating matrix for ending comparison
    def generate_board(self):
        board = []
        x = 1
        for i in range(0, self.row):
            r = []
            for j in range(0, self.column):
                if i == self.row - 1 and j == self.column - 1:
                    r.append(0)
                else:
                    r.append(x)
                x += 1
            board.append(r)
        return board

    # checking if we are not moving out of bounds of matrix
    def check_available_direction(self, d):
        if d not in 'LRUD':
            return False
        if self.zero_position[0] == self.row - 1 and d == 'D':
            return False
        if self.zero_position[1] == self.column - 1 and d == 'R':
            return False
        if self.zero_position[0] == 0 and d == 'U':
            return False
        if self.zero_position[1] == 0 and d == 'L':
            return False
        return True

    # checking if we are not moving backwards
    def check_previous_direction(self, d):
        if d == 'D' and self.previous == 'U':
            return False
        if d == 'U' and self.previous == 'D':
            return False
        if d == 'R' and self.previous == 'L':
            return False
        if d == 'L' and self.previous == 'R':
            return False
        return True

    # checking both possibilities
    def check_all_possible_moves(self, d):
        if self.check_previous_direction(d) and self.check_available_direction(d):
            return True
        else:
            return False

    def move(self, d):
        if d == "U":
            self.board[self.zero_position[0]][self.zero_position[1]], self.board[self.zero_position[0] - 1][self.zero_position[1]] = (
                self.board[self.zero_position[0] - 1][self.zero_position[1]],self.board[self.zero_position[0]][self.zero_position[1]])

        if d == "D":
            self.board[self.zero_position[0]][self.zero_position[1]], self.board[self.zero_position[0] + 1][self.zero_position[1]] = (
                self.board[self.zero_position[0] + 1][self.zero_position[1]],self.board[self.zero_position[0]][self.zero_position[1]])

        if d == "R":
            self.board[self.zero_position[0]][self.zero_position[1]], self.board[self.zero_position[0]][self.zero_position[1] + 1] = (
                self.board[self.zero_position[0]][self.zero_position[1] + 1],self.board[self.zero_position[0]][self.zero_position[1]])

        if d == "L":
            self.board[self.zero_position[0]][self.zero_position[1]], self.board[self.zero_position[0]][self.zero_position[1] - 1] = (
                self.board[self.zero_position[0]][self.zero_position[1] - 1], self.board[self.zero_position[0]][self.zero_position[1]])
        self.way += d
        self.depth += 1

    def __lt__(self, other):
        return self.depth < other.depth


