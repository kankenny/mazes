from moviepy import ImageSequenceClip, VideoFileClip  # type: ignore
from moviepy.video.fx import AccelDecel, Resize  # type: ignore

# moviepy does not provide type stubs


def postprocess_gif(
    file_name: str,
    duration: float,
    loop: int,
    dimension: tuple[int, int],
    fps: int = 30,
) -> None:
    """
    Postprocess a GIF file by resizing, adjusting duration, and looping.
    """
    clip = VideoFileClip(file_name)
    clip = Resize(dimension).apply(clip)
    clip = AccelDecel(new_duration=duration).apply(clip)
    clip.write_gif(file_name, fps=fps, loop=loop)


def postprocess_vid(
    frames,
    file_name: str,
    dimension: tuple[int, int],
    fps: int = 30,
) -> None:
    """
    Postprocess a video file by resizing and applying effects.
    """
    clip = ImageSequenceClip(frames, fps=fps)
    clip = Resize(dimension).apply(clip)
    clip = AccelDecel().apply(clip)
    clip.write_videofile(file_name, codec="mpeg4", fps=fps)
