#!/usr/bin/env python3
"""
Upload Brand HQ markdown files to Google Drive.
Creates folder structure inside 'Grouped Brand Discovery' and uploads all .md files.
"""

import os
import sys
import pickle
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Config
SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET = os.path.expanduser(
    '~/brandhq-listener/client_secret_250278094016-k1o55qraidamh1v82pgm4rstdlff0t8j.apps.googleusercontent.com.json'
)
TOKEN_FILE = os.path.expanduser('~/grouped_brand/.drive-token.pickle')
PARENT_FOLDER_ID = '1Xxf5FXOZaglTArxdbcs3P7f-hP1tMtWF'  # Grouped Brand Discovery
EXPORT_DIR = os.path.expanduser('~/grouped_brand/brand-hq-export')


def get_service():
    """Authenticate and return Drive service."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=8090, open_browser=False)
            print(f"\n>>> Open this URL in your browser to authorize:\n")
            # The URL is printed by run_local_server when open_browser=False
        with open(TOKEN_FILE, 'wb') as f:
            pickle.dump(creds, f)

    return build('drive', 'v3', credentials=creds)


def find_or_create_folder(service, name, parent_id):
    """Find existing folder or create new one."""
    query = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields='files(id, name)').execute()
    files = results.get('files', [])

    if files:
        print(f"  Found existing folder: {name}")
        return files[0]['id']

    metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=metadata, fields='id').execute()
    print(f"  Created folder: {name}")
    return folder['id']


def upload_file(service, filepath, parent_id):
    """Upload a file to Drive, replacing if it already exists."""
    filename = os.path.basename(filepath)

    # Check if file already exists
    query = f"name='{filename}' and '{parent_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields='files(id, name)').execute()
    existing = results.get('files', [])

    media = MediaFileUpload(filepath, mimetype='text/markdown', resumable=True)

    if existing:
        # Update existing file
        file = service.files().update(
            fileId=existing[0]['id'],
            media_body=media,
            fields='id, name'
        ).execute()
        print(f"  Updated: {filename}")
    else:
        # Create new file
        metadata = {
            'name': filename,
            'parents': [parent_id]
        }
        file = service.files().create(
            body=metadata,
            media_body=media,
            fields='id, name'
        ).execute()
        print(f"  Uploaded: {filename}")

    return file['id']


def main():
    print("Authenticating with Google Drive...")
    service = get_service()
    print("Authenticated!\n")

    # Create folder structure
    print("Setting up folder structure in 'Grouped Brand Discovery'...")
    brand_guide_id = find_or_create_folder(service, 'Brand Guide', PARENT_FOLDER_ID)
    archive_id = find_or_create_folder(service, 'Archive', PARENT_FOLDER_ID)

    # Upload top-level files (manifesto, quick-start)
    print("\nUploading top-level files...")
    for f in ['manifesto.md', 'quick-start.md']:
        filepath = os.path.join(EXPORT_DIR, f)
        if os.path.exists(filepath):
            upload_file(service, filepath, PARENT_FOLDER_ID)

    # Upload brand-guide section files
    print("\nUploading brand guide sections...")
    brand_guide_dir = os.path.join(EXPORT_DIR, 'brand-guide')
    for f in sorted(os.listdir(brand_guide_dir)):
        if f.endswith('.md'):
            filepath = os.path.join(brand_guide_dir, f)
            upload_file(service, filepath, brand_guide_id)

    # Upload archive files (if any)
    archive_dir = os.path.join(EXPORT_DIR, 'archive')
    archive_files = [f for f in os.listdir(archive_dir) if f.endswith('.md')] if os.path.exists(archive_dir) else []
    if archive_files:
        print("\nUploading archive files...")
        for f in sorted(archive_files):
            filepath = os.path.join(archive_dir, f)
            upload_file(service, filepath, archive_id)

    print("\n✅ Done! All files uploaded to Grouped Brand Discovery.")
    print(f"   Brand Guide: {len(os.listdir(brand_guide_dir))} sections")
    print(f"   Top-level: manifesto.md, quick-start.md")
    print(f"   Archive: {len(archive_files)} files")


if __name__ == '__main__':
    main()
