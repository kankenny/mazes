import random

from mazes.mazes.base_maze import BaseMaze


class Sidewinder(BaseMaze):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)

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
                    member = random.sample(run_list, k=1)[0]
                    if member.north_cell:
                        member.link(member.north_cell)
                    run_list.clear()
                else:
                    cell.link(cell.east_cell)  # type: ignore[arg-type]
