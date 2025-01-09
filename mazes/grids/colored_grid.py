from PIL import Image, ImageDraw

from mazes.heuristics.distances import Distances
from mazes.util.colors import get_rgb

from .basic_grid import BasicGrid


class ColoredGrid(BasicGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        self.distances = None

    @property
    def distances(self) -> Distances | None:
        return self._distances

    @distances.setter
    def distances(self, distances: Distances) -> None:
        self._distances = distances

    def background_color_for(self, cell, color):
        farthest_cell, max_dist = self.distances.max()

        distance = self.distances.cells.get(cell, 0.1)
        intensity = distance / max_dist

        if isinstance(color, tuple):
            color_values = color
        else:
            r_unscaled, g_unscaled, b_unscaled = get_rgb(color)
            color_values = (r_unscaled, g_unscaled, b_unscaled)

        r, g, b = [
            round((1 - intensity) * 255 + intensity * value) for value in color_values
        ]

        return r, g, b

    def to_png(
        self, cell_size: int = 10, output_name: str = "maze.png", cell_color=(255, 0, 0)
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
                    color = self.background_color_for(cell, cell_color)
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
