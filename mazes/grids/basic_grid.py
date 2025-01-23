import random
from typing import Generator, Iterator

import numpy as np
from PIL import Image, ImageDraw

from mazes.cells import BasicCell
from mazes.util.vid_processors import postprocess_gif, postprocess_vid


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

    def background_color_for(self, cell: BasicCell) -> tuple[int, int, int] | None:
        return None

    def to_png(
        self,
        cell_size: int = 15,
        wall_thickness: int = 1,
        output_name: str = "maze.png",
    ) -> None:
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
                        draw.line([x1, y1, x2, y1], wall, wall_thickness, None)
                    if not cell.west_cell:
                        draw.line([x1, y1, x1, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.east_cell):  # type: ignore[arg-type]
                        draw.line([x2, y1, x2, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.south_cell):  # type: ignore[arg-type]
                        draw.line([x1, y2, x2, y2], wall, wall_thickness, None)

        img.show()
        img.save(output_name)

    def to_gif(
        self,
        cell_size: int = 15,
        wall_thickness: int = 1,
        duration=5,
        loop=0,
        output_name: str = "maze.gif",
    ) -> None:
        """
        Collect the frame by frame creation or traversal of a maze
        and saves a gif format of it
        """
        SIZE_FACTOR = 2.5
        cell_size = int(cell_size * SIZE_FACTOR)

        frames = []

        img_width = cell_size * self.cols
        img_height = cell_size * self.rows

        background = (255, 255, 255)
        wall = (0, 0, 0)

        img_dimension = (img_width + 1, img_height + 1)

        img = Image.new("RGBA", img_dimension, background)
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
                        draw.line([x1, y1, x2, y1], wall, wall_thickness, None)
                    if not cell.west_cell:
                        draw.line([x1, y1, x1, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.east_cell):  # type: ignore[arg-type]
                        draw.line([x2, y1, x2, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.south_cell):  # type: ignore[arg-type]
                        draw.line([x1, y2, x2, y2], wall, wall_thickness, None)

                frames.append(img.copy())

        frames[0].save(
            output_name,
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=0,
            loop=loop,
        )

        postprocess_gif(output_name, duration, loop, img_dimension)

    def to_vid(
        self,
        cell_size: int = 15,
        wall_thickness: int = 1,
        duration=5,
        output_name: str = "maze.mp4",
    ) -> None:
        """
        Collect the frame by frame creation or traversal of a maze
        and saves a gif format of it
        """
        SIZE_FACTOR = 2.5
        cell_size = int(cell_size * SIZE_FACTOR)

        frames = []

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
                        draw.line([x1, y1, x2, y1], wall, wall_thickness, None)
                    if not cell.west_cell:
                        draw.line([x1, y1, x1, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.east_cell):  # type: ignore[arg-type]
                        draw.line([x2, y1, x2, y2], wall, wall_thickness, None)
                    if not cell.is_linked(cell.south_cell):  # type: ignore[arg-type]
                        draw.line([x1, y2, x2, y2], wall, wall_thickness, None)

                frames.append(np.array(img.copy()))

        postprocess_vid(frames, output_name)

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

    def dead_ends(self) -> list[BasicCell]:
        deadend_cells = [c for c in self.iter_each_cell() if len(c.links) == 1]

        return deadend_cells

    # def init_mask(self) -> None:
    #     self.bits: list[list[bool]] = [
    #         [True for _ in range(self.cols)] for _ in range(self.rows)
    #     ]
