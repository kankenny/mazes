from typing import Iterator, Optional

from mazes.cells.basic_cell import BasicCell


class BasicGrid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.cols: int = cols

        self.grid: list[list[BasicCell]] = self.prepare_grid(
            self.rows, self.cols)
        self.prepare_cells(self.grid)

    def __getitem__(self, index: tuple[int, int]) -> BasicCell | None:
        """
        Overload the grid indexing operator. Validates row and column indices.
        """
        row, col = index

        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.cols:
            return None

        return self.grid[row][col]

    def __len__(self) -> int:
        return self.rows * self.cols

    def __iter__(self) -> Iterator[BasicCell | None]:
        """
        Initialize the iterator to start at the top-left corner of the grid.
        """
        self._row = 0
        self._col = 0
        return self

    def __next__(self) -> Optional[BasicCell]:
        """
        Return the next cell in the grid. Raise StopIteration when all
        cells are visited.
        """
        if self._row < self.rows:
            cell = self[self._row, self._col]

            self._col += 1
            if self._col == self.cols:
                self._col = 0
                self._row += 1

            return cell
        else:
            raise StopIteration

    @staticmethod
    def prepare_grid(rows: int, cols: int) -> list[list[BasicCell]]:
        grid: list[list[BasicCell]] = []
        for r in range(rows):
            row = [BasicCell(r, c) for c in range(cols)]
            grid.append(row)
        return grid

    def prepare_cells(self, grid) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self[row, col]
                if cell:
                    cell.north_cell = self[row - 1, col]
                    cell.south_cell = self[row + 1, col]
                    cell.east_cell = self[row, col + 1]
                    cell.west_cell = self[row, col - 1]
