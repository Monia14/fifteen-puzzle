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
        self.f = False

    def dfs(self):
        start = time.time()
        stack = []
        stack.append(Matrix(self.board, self.row, self.column, 0, "", ""))
        while stack and not self.f:
            current_node = stack.pop()
            stack_reversed = []
            for d in self.order:
                if current_node.check_all_possible_moves(d) and current_node.depth < MAX_DEPTH:
                    next_node = Matrix(current_node.board, self.row, self.column, current_node.depth,
                                       current_node.way, d)

                    next_node.move(d)
                    # print("kierunek: ", d)
                    # print(next_node.board)
                    self.visited += 1
                    next_node.zero_position = next_node.find_zero_field()

                    if next_node.depth > self.depth:
                        self.depth = next_node.depth
                    if next_node.board.tobytes() == next_node.result.tobytes():
                        end = time.time()
                        self.time = end - start
                        self.sequence = next_node.way
                        self.f = True
                    else:
                        stack_reversed.append(next_node)
            stack_reversed.reverse()
            self.processed += 1
            for elem in stack_reversed:
                stack.append(elem)
















