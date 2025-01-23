import random
from random import choice

from mazes.grids import BasicGrid
from mazes.mazes.base_maze import BaseMaze
from mazes.util.maze_profiler import maze_profiler


@maze_profiler
class Sidewinder(BaseMaze):
    def __call__(self) -> BasicGrid:
        for row in self.grid.iter_each_rows():
            run_list = []

            for cell in row:
                run_list.append(cell)

                at_eastern_boundary = cell.east_cell is None
                at_nortern_boundary = cell.north_cell is None

                should_close_out = at_eastern_boundary or (
                    not at_nortern_boundary and random.randint(0, 2) == 0
                )

                if should_close_out:
                    member = choice(run_list)
                    if member.north_cell:
                        member.link(member.north_cell)
                    run_list.clear()
                else:
                    if cell.east_cell:
                        cell.link(cell.east_cell)

        return self.grid
