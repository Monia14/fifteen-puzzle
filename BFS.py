import time
from collections import deque

from Matrix import *
import numpy

class BFS:
    def __init__(self, board, result, order, row, column):
        self.board = board
        self.order = order
        self.result = result
        self.row = row
        self.column = column

        self.sequence = ""
        self.depth = 0
        self.visited = 0
        self.processed = 0
        self.time = 0
        self.finished = False

    def bfs(self):
        start = time.time()
        queue = []
        queue.append(Matrix(self.board, self.row, self.column, 0, "", ""))
        while queue:
            current_node = queue.pop(0)
            if current_node.board.tobytes() == current_node.result.tobytes():
                end = time.time()
                self.time = end - start
                self.sequence = current_node.way
                self.depth = current_node.depth
                return
            for d in self.order:
                if current_node.check_all_possible_moves(d):
                    next_node = Matrix(current_node.board, self.row, self.column, current_node.depth, current_node.way, d)
                    next_node.move(d)
                    next_node.zero_position = next_node.find_zero_field()
                    queue.append(next_node)
                    self.visited += 1
            self.processed += 1










