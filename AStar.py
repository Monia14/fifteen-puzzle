import time
from Matrix import *
from queue import PriorityQueue


def hamm(node):
    dist = 0
    for i in range(node.row):
        for j in range(node.column):
            if node.board[i][j] != node.result[i][j] and node.board[i][j] != 0:
                dist += 1

    return dist


def manh(node):
    dist = 0
    for i in range(node.row):
        for j in range(node.column):
            if node.board[i][j] != 0:
                col = (node.board[i][j] - 1) // node.column
                row = (node.board[i][j] - 1) % node.row
                dist += abs(i - col) + abs(j - row)

    return dist


class AStar:
    def __init__(self, board, result, row, column, h):
        self.board = board
        self.order = ['L', 'D', 'R', 'U']
        self.result = result
        self.row = row
        self.column = column
        self.h = h

        self.sequence = ""
        self.depth = 0
        self.visited = 0
        self.processed = 0
        self.time = 0

    def choose_heuristic(self, node):
        if self.h == "manh":
            return manh(node)
        if self.h == "hamm":
            return hamm(node)

    def astar(self):
        start = time.time()
        priority = PriorityQueue()
        root = Matrix(self.board, self.row, self.column, 0, "", "")
        priority.put((0, root))
        while priority:
            current_node = priority.get()[1]
            if current_node.board.tobytes() == current_node.result.tobytes():
                end = time.time()
                self.time = end - start
                self.sequence = current_node.way
                self.depth = current_node.depth
                return
            for d in self.order:
                if current_node.check_all_possible_moves(d):
                    next_node = Matrix(current_node.board, self.row, self.column, current_node.depth, current_node.way,
                                       d)
                    next_node.move(d)
                    next_node.zero_position = next_node.find_zero_field()
                    if next_node.depth > self.depth:
                        self.depth = next_node.depth

                    value = next_node.depth + self.choose_heuristic(next_node)
                    priority.put((value, next_node))
                    self.visited += 1
            self.processed += 1
