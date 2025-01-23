from random import choice
from typing import Optional

from mazes.cells.basic_cell import BasicCell
from mazes.grids.basic_grid import BasicGrid
from mazes.mazes.base_maze import BaseMaze


class DepthFirstSearch(BaseMaze):
    def __call__(self, starting_cell: Optional[BasicCell] = None) -> BasicGrid:
        if starting_cell is None:
            starting_cell = self.grid.random_cell()

        stack = []
        stack.append(starting_cell)

        while stack:
            current = stack[-1]
            neighbors = [n for n in current.neighbors if not n.links]

            if neighbors:
                neighbor = choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
            else:
                stack.pop()

        return self.grid
