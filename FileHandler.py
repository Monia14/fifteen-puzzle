class FileHandler:
    file = ""
    board = []
    size = []

    def __init__(self, file, file_output, file_stats):
        self.file = file
        self.file_output = file_output
        self.file_stats = file_stats

    def readBoard(self):
        with open(self.file, 'r') as reader:
            first_line = True
            for line in reader:
                if first_line:
                    self.size = line.split()
                    first_line = False
                else:
                    self.board.append(line.split())

    def writeOutput(self, sequence, length):
        with open(self.file_output, 'w') as writer:
            if sequence == '-1':
                writer.write(sequence)
            else:
                writer.write(str(length) + '\n')
                writer.write(sequence + '\n')

    def writeStats(self, length, visited, processed, depth, time):
        with open(self.file_stats, 'w') as writer:
            writer.write(str(length) + '\n')
            writer.write(str(visited) + '\n')
            writer.write(str(processed) + '\n')
            writer.write(str(depth) + '\n')
            writer.write(str(time) + '\n')

