from moviepy import ImageSequenceClip, VideoFileClip  # type: ignore
from moviepy.video.fx import AccelDecel  # type: ignore

# moviepy does not provide type stubs


def postprocess_gif(
    file_name: str,
    duration: float,
    loop: int,
    dimension: tuple[int, int],
    fps: int = 30,
) -> None:
    clip = VideoFileClip(file_name)
    clip = AccelDecel(new_duration=duration).apply(clip)
    clip.write_gif(file_name, fps=30, loop=loop)


def postprocess_vid(
    frames,
    file_name: str,
    fps: int = 30,
) -> None:
    clip = ImageSequenceClip(frames, fps=fps)
    clip = AccelDecel().apply(clip)
    clip.write_videofile(file_name, codec="mpeg4", fps=fps)
