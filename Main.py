import sys

from DFS import *
from Matrix import *
from BFS import *
from AStar import *
from FileHandler import *


# converting fields from str to int
def convert_board(board):
    converted = []
    for row in board:
        r = []
        for elem in row:
            r.append(int(elem))
        converted.append(r)

    return converted


def get_order(param):
    order = []
    for letter in param:
        order.append(letter)
    return order


def main():
    if len(sys.argv) != 6:
        sys.exit(" Podano bledna ilosc argumentow!")

    algorithm = sys.argv[1]
    param = sys.argv[2]
    file_handler = FileHandler(sys.argv[3], sys.argv[4], sys.argv[5])

    file_handler.readBoard()
    puzzle = convert_board(file_handler.board)
    board = Matrix(puzzle, int(file_handler.size[0]), int(file_handler.size[1]), 0, "", "")

    print(" wczytana tablica: ", board.board)
    print(" końcowa tablica: ", board.result)

    if algorithm == "bfs":
        bfs = BFS(board.board, board.result, get_order(param), board.row, board.column)
        bfs.bfs()
        sequence, len_sequence, depth, visited, processed, time = bfs.sequence, len(bfs.sequence), bfs.depth, \
                                                                  bfs.visited, bfs.processed, bfs.time

    if algorithm == "dfs":
        dfs = DFS(board.board, board.result, get_order(param), board.row, board.column)
        dfs.dfs()
        sequence, len_sequence, depth, visited, processed, process_time = dfs.sequence, len(dfs.sequence), dfs.depth, \
                                                                          dfs.visited, dfs.processed, dfs.time
    if algorithm == "astr":
        astar = AStar(board.board, board.result, board.row, board.column, param)
        astar.astar()
        sequence, len_sequence, depth, visited, processed, process_time = astar.sequence, len(
            astar.sequence), astar.depth, \
                                                                          astar.visited, astar.processed, astar.time

    print("rozwiązanie:", sequence)
    if sequence == '-1':
        len_sequence = -1
    process_time = round(process_time * 1000, 3)
    print("długość znalezionego rozwiązania: ", len_sequence)
    print("maksymalna głębokość rekursji: ", depth)
    print("liczba stanów odwiedzonych: ", visited)
    print("liczba stanów przetworzonych: ", processed)
    print("czas trwania: ", process_time, "ms")
    file_handler.writeOutput(sequence, len_sequence)
    file_handler.writeStats(len_sequence, visited, processed, depth, process_time)


if __name__ == "__main__":
    main()
