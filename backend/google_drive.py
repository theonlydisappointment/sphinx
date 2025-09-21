"""Google Drive storage utilities."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

from .config import settings


SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def _get_service() -> Any:
    """Authenticate and return a Drive service client."""
    credentials = service_account.Credentials.from_service_account_file(
        settings.google_credentials, scopes=SCOPES
    )
    return googleapiclient.discovery.build("drive", "v3", credentials=credentials)


def upload_file(file_path: Path, mime_type: str = "video/mp4") -> str:
    """Upload a file and return its Drive file ID."""
    service = _get_service()
    metadata = {"name": file_path.name}
    media = MediaFileUpload(file_path.as_posix(), mimetype=mime_type)
    file = service.files().create(body=metadata, media_body=media, fields="id").execute()
    return file["id"]
