# Oracle MVP

Oracle is an automation platform for digital creators. This repository contains a minimal backend prototype and supporting assets.

## Contents
- `backend/` – Python modules for video generation, social posting, and integrations.
- `configs/` – Supabase schema and API endpoint configuration.
- `postman/` – Postman collection for API testing.
- `frontend/` – Layout description for the Webflow frontend.
- `docs/` – Automation blueprints and additional docs.

## Quick Start
1. Set environment variables for API keys (see `backend/config.py`).
2. Install dependencies:
   ```bash
   pip install moviepy gtts supabase py google-api-python-client stripe requests
   ```
3. Run a pipeline example:
   ```python
   from pathlib import Path
   from backend.automations import text_to_social_pipeline

   text_to_social_pipeline("user-uuid", "Hello world", Path("background.mp4"))
   ```
