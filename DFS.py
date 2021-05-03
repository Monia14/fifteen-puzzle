import time
from collections import deque

from Matrix import *
import numpy
MAX_DEPTH = 20
class DFS:
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

    def dfs(self):
        start = time.time()
        stack = []
        stack.append(Matrix(self.board, self.row, self.column, 0, "", ""))
        while stack:
            stack_reversed = []
            current_node = stack.pop()
            if current_node.board.tobytes() == current_node.result.tobytes():
                end = time.time()
                self.time = end - start
                self.sequence = current_node.way
                return
            if current_node.depth < MAX_DEPTH:
                for d in self.order:
                    if current_node.check_all_possible_moves(d):
                        next_node = Matrix(current_node.board, self.row, self.column, current_node.depth,
                                           current_node.way, d)
                        next_node.move(d)
                        next_node.zero_position = next_node.find_zero_field()
                        stack_reversed.append(next_node)
                        if next_node.depth > self.depth:
                            self.depth = next_node.depth

                self.processed += 1
                stack_reversed.reverse()
                for elem in stack_reversed:
                    stack.append(elem)
                    self.visited += 1











