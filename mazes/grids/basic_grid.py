import random
from typing import Generator, Iterator

from PIL import Image, ImageDraw

from mazes.cells.basic_cell import BasicCell


class BasicGrid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.cols: int = cols

        self.grid: list[list[BasicCell]] = self.prepare_grid(self.rows, self.cols)
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

    def __next__(self) -> BasicCell | None:
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

    def __str__(self) -> str:
        output = "\n+" + "---+" * self.cols + "\n"
        corner = "+"

        for row in self.iter_each_rows():
            top = "|"
            bottom = "+"

            for cell in row:
                body = f" {self.contents_of(cell)} "
                east_boundary: str = " " if cell.is_linked(cell.east_cell) else "|"  # type: ignore[arg-type]
                top = top + body + east_boundary

                south_boundary: str = (
                    "   " if cell.is_linked(cell.south_cell) else "---"  # type: ignore[arg-type]
                )
                bottom = bottom + south_boundary + corner

            output = output + top + "\n"
            output = output + bottom + "\n"

        return output

    def contents_of(self, cell: BasicCell) -> str:
        return " "

    def background_color_for(self, cell) -> tuple[int, int, int] | None:
        return None

    def to_png(self, cell_size: int = 10, output_name: str = "maze.png") -> None:
        img_width = cell_size * self.cols
        img_height = cell_size * self.rows

        background = (255, 255, 255)
        wall = (0, 0, 0)

        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)

        for draw_mode in range(2):
            for cell in self.iter_each_cell():
                x1 = cell.col * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.col + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                if draw_mode == 0:  # Background Mode
                    color = self.background_color_for(cell)
                    draw.rectangle((x1, y1, x2, y2), fill=color)
                else:  # Wall Mode
                    if not cell.north_cell:
                        draw.line([x1, y1, x2, y1], wall, 1, None)
                    if not cell.west_cell:
                        draw.line([x1, y1, x1, y2], wall, 1, None)
                    if not cell.is_linked(cell.east_cell):  # type: ignore[arg-type]
                        draw.line([x2, y1, x2, y2], wall, 1, None)
                    if not cell.is_linked(cell.south_cell):  # type: ignore[arg-type]
                        draw.line([x1, y2, x2, y2], wall, 1, None)

        img.show()
        img.save(output_name)

    def random_cell(self) -> BasicCell:
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)

        return self[row, col]  # type: ignore[return-value]

    def iter_each_rows(self) -> Generator[list[BasicCell], None, None]:
        for i in range(self.rows):
            yield self.grid[i][:]

    def iter_each_cell(self) -> Generator[BasicCell, None, None]:
        for row in self.iter_each_rows():
            for cell in row:
                yield cell

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
