from random import choice

from mazes.grids import MaskedGrid
from mazes.util import maze_profiler

from .masked_base_maze import MaskedBaseMaze


@maze_profiler
class MaskedAldousBroder(MaskedBaseMaze):
    def __call__(self) -> MaskedGrid:
        cell = self.grid.random_cell()
        unvisited = self.grid.mask.count() - 1

        while unvisited > 0:
            neighbor = choice(cell.neighbors)

            if len(neighbor.get_links()) == 0:
                cell.link(neighbor)
                unvisited = unvisited - 1

            cell = neighbor

        return self.grid
