"""Text-to-video generation pipeline."""
from __future__ import annotations

import os
from pathlib import Path

import moviepy.editor as mpy
import requests

from .config import settings


def _synthesize_audio(text: str, out_path: Path) -> Path:
    """Generate a simple audio track using gTTS (placeholder)."""
    try:
        from gtts import gTTS
    except ImportError as exc:  # pragma: no cover - runtime guard
        raise RuntimeError("gTTS is required for audio synthesis") from exc

    tts = gTTS(text)
    tts.save(out_path.as_posix())
    return out_path


def generate_video(text: str, background_video: Path, output_path: Path) -> Path:
    """Generate a captioned video and convert via CloudConvert."""
    audio_file = _synthesize_audio(text, output_path.with_suffix(".mp3"))

    clip = mpy.VideoFileClip(background_video.as_posix()).subclip(0, 15)
    clip = clip.set_audio(mpy.AudioFileClip(audio_file.as_posix()))
    caption = mpy.TextClip(text, fontsize=50, color="white", method="caption", size=clip.size)
    caption = caption.set_duration(clip.duration).set_pos("center")
    final = mpy.CompositeVideoClip([clip, caption])
    temp_video = output_path.with_suffix(".temp.mp4")
    final.write_videofile(temp_video.as_posix(), codec="libx264", audio_codec="aac")

    # Upload to CloudConvert for final processing
    with open(temp_video, "rb") as f:
        response = requests.post(
            "https://api.cloudconvert.com/v2/import/upload",
            headers={"Authorization": f"Bearer {settings.cloudconvert_api_key}"},
            files={"file": f},
        )
        response.raise_for_status()

    os.replace(temp_video, output_path)
    audio_file.unlink(missing_ok=True)
    return output_path
