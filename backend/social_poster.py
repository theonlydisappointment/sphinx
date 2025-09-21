"""Social network posting utilities."""
from __future__ import annotations

from pathlib import Path
from typing import Dict

import requests

from .config import settings


def post_to_instagram(video_path: Path, caption: str) -> Dict[str, str]:
    """Upload a video to Instagram using the Graph API."""
    url = "https://graph.facebook.com/v17.0/me/media"
    with open(video_path, "rb") as f:
        files = {"video_file": f}
        data = {"caption": caption, "access_token": settings.instagram_token}
        response = requests.post(url, files=files, data=data, timeout=30)
    response.raise_for_status()
    return response.json()


def post_to_discord(video_path: Path, caption: str) -> Dict[str, str]:
    """Send a video to a Discord channel via webhook."""
    with open(video_path, "rb") as f:
        response = requests.post(
            settings.discord_webhook,
            data={"content": caption},
            files={"file": f},
            timeout=30,
        )
    response.raise_for_status()
    return response.json()
