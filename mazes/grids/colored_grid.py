from PIL import Image, ImageDraw

from mazes.heuristics.distances import Distances
from mazes.util.colors import get_rgb
from mazes.util.vid_optimizer import optimize_gif

from .distance_grid import DistanceGrid


class ColoredGrid(DistanceGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        self.distances = None

    @property  # type: ignore[override]
    def distances(self) -> Distances | None:
        return self._distances

    @distances.setter
    def distances(self, distances: Distances) -> None:
        self._distances = distances

    def background_color_for(self, cell, color):
        farthest_cell, max_dist = self.distances.max()

        distance = self.distances.cells.get(cell, 0)
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

    def background_distance_for(self, cell) -> str:
        if self.distances is not None:
            dist_str = str(self.distances[cell])
        else:
            dist_str = "0"

        return dist_str

    def to_png(
        self,
        cell_size: int = 15,
        output_name: str = "maze.png",
        display_distances: bool = False,
        cell_color: tuple[int, int, int] = (255, 0, 0),
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

                    if display_distances:
                        dist = self.background_distance_for(cell)
                        text_bbox = draw.textbbox((0, 0), dist)
                        text_width = text_bbox[2] - text_bbox[0]
                        text_height = text_bbox[3] - text_bbox[1]

                        text_x = (x1 + x2 - text_width) / 2
                        text_y = (y1 + y2 - text_height) / 2

                        draw.text((text_x, text_y), text=dist, fill="black")
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

    def to_gif(
        self,
        cell_size: int = 15,
        duration=5,
        loop=1,
        output_name: str = "maze.gif",
        display_distances: bool = False,
        cell_color: tuple[int, int, int] = (255, 0, 0),
    ) -> None:  # type: ignore[override]
        """
        Collect the frame by frame creation or traversal of a maze
        and saves a gif format of it
        """
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
                    color = self.background_color_for(cell, cell_color)
                    draw.rectangle((x1, y1, x2, y2), fill=color)

                    if display_distances:
                        dist = self.background_distance_for(cell)
                        text_bbox = draw.textbbox((0, 0), dist)
                        text_width = text_bbox[2] - text_bbox[0]
                        text_height = text_bbox[3] - text_bbox[1]

                        text_x = (x1 + x2 - text_width) / 2
                        text_y = (y1 + y2 - text_height) / 2

                        draw.text((text_x, text_y), text=dist, fill="black")
                else:  # Wall Mode
                    if not cell.north_cell:
                        draw.line([x1, y1, x2, y1], wall, 1, None)
                    if not cell.west_cell:
                        draw.line([x1, y1, x1, y2], wall, 1, None)
                    if not cell.is_linked(cell.east_cell):  # type: ignore[arg-type]
                        draw.line([x2, y1, x2, y2], wall, 1, None)
                    if not cell.is_linked(cell.south_cell):  # type: ignore[arg-type]
                        draw.line([x1, y2, x2, y2], wall, 1, None)

                frames.append(img.copy())

        frames[0].save(
            output_name,
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=0,
            loop=loop,
        )

        optimize_gif(output_name, duration, loop)
