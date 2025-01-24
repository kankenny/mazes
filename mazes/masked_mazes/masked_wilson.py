from random import choice

from mazes.grids import MaskedGrid
from mazes.masked_mazes.masked_base_maze import MaskedBaseMaze
from mazes.util.maze_profiler import maze_profiler


@maze_profiler
class MaskedWilson(MaskedBaseMaze):
    def __call__(self) -> MaskedGrid:
        unvisited = [c for c in self.grid.iter_each_cell()]

        first = choice(unvisited)
        unvisited.remove(first)

        while unvisited:
            cell = choice(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = choice(cell.neighbors)

                if cell in path:
                    loop_start = path.index(cell)
                    path = path[: loop_start + 1]
                else:
                    path.append(cell)

            for i in range(len(path) - 1):
                path[i].link(path[i + 1])
                unvisited.remove(path[i])

        return self.grid
