from random import choice

from mazes.grids import BasicGrid
from mazes.mazes.base_maze import BaseMaze
from mazes.util.maze_profiler import maze_profiler


@maze_profiler
class Wilson(BaseMaze):
    def __call__(self) -> BasicGrid:
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
