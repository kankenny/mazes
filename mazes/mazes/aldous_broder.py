from random import choice

from mazes.grids.basic_grid import BasicGrid
from mazes.mazes.base_maze import BaseMaze


class AldousBroder(BaseMaze):
    def __call__(self) -> BasicGrid:
        cell = self.grid.random_cell()
        unvisited = len(self.grid) - 1

        while unvisited > 0:
            neighbor = choice(cell.neighbors)

            if len(neighbor.get_links()) == 0:
                cell.link(neighbor)
                unvisited = unvisited - 1

            cell = neighbor

        return self.grid
