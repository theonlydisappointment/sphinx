"""Configuration helpers for Oracle backend."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Settings:
    """Application settings loaded from environment variables."""

    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_key: str = os.getenv("SUPABASE_KEY", "")
    stripe_api_key: str = os.getenv("STRIPE_API_KEY", "")
    google_credentials: str = os.getenv("GOOGLE_CREDENTIALS", "")
    instagram_token: str = os.getenv("INSTAGRAM_TOKEN", "")
    discord_webhook: str = os.getenv("DISCORD_WEBHOOK", "")
    cloudconvert_api_key: str = os.getenv("CLOUDCONVERT_API_KEY", "")


settings = Settings()
