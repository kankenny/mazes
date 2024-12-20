from random import choice

from mazes.grids.basic_grid import BasicGrid
from mazes.mazes.base_maze import BaseMaze


class BinaryTree(BaseMaze):
    def __call__(self) -> BasicGrid:
        for cell in self.grid.iter_each_cell():
            neighbors = []

            if cell.north_cell:
                neighbors.append(cell.north_cell)
            if cell.east_cell:
                neighbors.append(cell.east_cell)

            if len(neighbors) != 0:
                neighbor = choice(neighbors)

            if neighbor:
                cell.link(neighbor)

        return self.grid
