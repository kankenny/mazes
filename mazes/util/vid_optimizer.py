from moviepy import VideoFileClip  # type: ignore
from moviepy.video.fx import AccelDecel, Resize  # type: ignore


def optimize_gif(
    file_name: str,
    duration: float,
    loop: int,
    dimension: tuple[int, int],
    fps: int = 30,
) -> None:
    clip = VideoFileClip(file_name)
    clip = Resize(dimension).apply(clip)
    clip = AccelDecel(new_duration=duration).apply(clip)
    clip.write_gif(file_name, fps=30, loop=loop)
