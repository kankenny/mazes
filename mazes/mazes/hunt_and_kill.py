from random import choice
from typing import Optional

from mazes.cells import BasicCell
from mazes.grids import BasicGrid
from mazes.mazes.base_maze import BaseMaze
from mazes.util.maze_profiler import maze_profiler


@maze_profiler
class HuntAndKill(BaseMaze):
    def __call__(self) -> BasicGrid:
        current: Optional[BasicCell] = self.grid.random_cell()

        while current:
            unvisited_neighbors = [n for n in current.neighbors if not n.links]

            if unvisited_neighbors:
                neighbor = choice(unvisited_neighbors)
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in self.grid.iter_each_cell():
                    visited_neighbors = [n for n in cell.neighbors if n.links]
                    if len(cell.links) == 0 and visited_neighbors:
                        current = cell

                        neighbor = choice(visited_neighbors)
                        current.link(neighbor)

                        break

        return self.grid
