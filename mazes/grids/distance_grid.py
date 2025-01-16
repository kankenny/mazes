from PIL import Image, ImageDraw

from mazes.util.vid_optimizer import optimize_gif

from .basic_grid import BasicGrid


class DistanceGrid(BasicGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        self.distances = None

    def contents_of(self, cell) -> str:
        if self.distances is not None and cell in self.distances.cells:
            return str_base(self.distances[cell], 36)
        else:
            return super().contents_of(cell)

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
            optimize=True,
            duration=0,
            loop=loop,
        )

        optimize_gif(output_name, duration, loop, img_dimension)


# With help of https://github.com/crux888 and his similar repo
# (from https://stackoverflow.com/questions/2063425)


def str_base(number, base):
    if number < 0:
        return "-" + str_base(-number, base)
    else:
        (d, m) = divmod(number, base)
        if d:
            return str_base(d, base) + digit_to_char(m)
        else:
            return digit_to_char(m)


def digit_to_char(digit):
    if digit < 10:
        return chr(ord("0") + digit)
    else:
        return chr(ord("a") + digit - 10)
