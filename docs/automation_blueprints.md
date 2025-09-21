# Automation Blueprints

## Video Pipeline
1. Receive caption text from user.
2. `backend.video_generator.generate_video` creates video with captions and voiceover.
3. Upload final MP4 to Google Drive via `backend.google_drive.upload_file`.
4. Post video to Instagram and Discord using `backend.social_poster`.
5. Record video metadata in Supabase with `backend.supabase_db.insert_video`.

## Error Handling
- Exceptions are propagated to calling Make.com scenario.
- Use retries for network requests.

## Logging
- Each step should log structured events to a log service or Supabase table (not implemented).
