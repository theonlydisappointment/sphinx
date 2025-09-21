"""Supabase database helpers."""
from __future__ import annotations

from typing import Any, Dict

from supabase import Client, create_client

from .config import settings


def get_client() -> Client:
    """Instantiate a Supabase client using settings."""
    return create_client(settings.supabase_url, settings.supabase_key)


def insert_video(client: Client, owner_id: str, caption: str, file_url: str) -> Dict[str, Any]:
    """Insert a generated video record."""
    data = {
        "owner_id": owner_id,
        "caption": caption,
        "file_url": file_url,
        "status": "ready",
    }
    return client.table("videos").insert(data).execute().data  # type: ignore[no-any-return]


def fetch_payments(client: Client, user_id: str) -> Dict[str, Any]:
    """Fetch payment records for a user."""
    return client.table("payments").select("*").eq("user_id", user_id).execute().data  # type: ignore[no-any-return]
