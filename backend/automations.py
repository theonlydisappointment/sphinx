"""Automation blueprints for Oracle."""
from __future__ import annotations

from pathlib import Path

from . import google_drive, social_poster, supabase_db, video_generator


def text_to_social_pipeline(owner_id: str, caption: str, background: Path) -> str:
    """Generate a video from text and publish to social platforms."""
    output = Path("/tmp/output.mp4")
    video_path = video_generator.generate_video(caption, background, output)
    drive_id = google_drive.upload_file(video_path)
    client = supabase_db.get_client()
    supabase_db.insert_video(client, owner_id, caption, f"https://drive.google.com/file/d/{drive_id}")
    social_poster.post_to_instagram(video_path, caption)
    social_poster.post_to_discord(video_path, caption)
    return drive_id
