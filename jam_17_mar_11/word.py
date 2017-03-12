import sys
import numpy as np
from util import SolverBase


class WordSolver(SolverBase):

    def __call__(self):
        result = []
        for i, line in self._enumerate_input():
            grid_max, n = (int(p) for p in line.split(" "))
            gen = IOGenerator(grid_max, n)
            grid = gen.grid()
            result.append(grid)
        self._write_result(result, "\n")


class IOGenerator(object):
    horizontal_pattern = "I/O"

    def __init__(self, grid_max, n):
        self.grid_max = grid_max
        self.n = n
        self.max_num_per_line = None
        if n != 0:
            self.max_num_per_line = int(np.floor(self.grid_max / 3))

    def grid(self):
        if self.n == 0:
            return "IO"
        elif self.n <= self.max_num_per_line:
            return self.horizontal_pattern * self.n
        full_line = self.horizontal_pattern * self.max_num_per_line
        result = [full_line]
        n = self.n - self.max_num_per_line
        while n > 0:
            line_len = len(result[0])
            result.append("O"*line_len)
            if n >= self.max_num_per_line:
                result.append(full_line)
                n -= self.max_num_per_line
            else:
                line = self.horizontal_pattern * n
                line += 'O' * (line_len - len(line))
                result.append(line)
                break
            if len(result) == self.grid_max:
                raise ValueError("error")
        return "\n".join(result)


if __name__ == "__main__":
    # python word.py C-small-practice
    WordSolver(sys.argv[1])()
