#!/usr/bin/env python3
"""
Set up the full Brand HQ folder structure in Google Drive.
- Renames 'Grouped Brand Discovery' → 'Grouped Brand HQ'
- Creates missing subfolders for the full StarSuite ecosystem
"""

import os
import pickle
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN_FILE = os.path.expanduser('~/grouped_brand/.drive-token.pickle')
PARENT_FOLDER_ID = '1Xxf5FXOZaglTArxdbcs3P7f-hP1tMtWF'  # Grouped Brand Discovery


SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET = os.path.expanduser(
    '~/brandhq-listener/client_secret_250278094016-k1o55qraidamh1v82pgm4rstdlff0t8j.apps.googleusercontent.com.json'
)

def get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=8090, open_browser=False)
        with open(TOKEN_FILE, 'wb') as f:
            pickle.dump(creds, f)
    return build('drive', 'v3', credentials=creds)


def find_or_create_folder(service, name, parent_id):
    query = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields='files(id, name)').execute()
    files = results.get('files', [])
    if files:
        print(f"  ✓ Already exists: {name}")
        return files[0]['id']
    metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=metadata, fields='id').execute()
    print(f"  + Created: {name}")
    return folder['id']


def main():
    print("Connecting to Google Drive...\n")
    service = get_service()

    # 1. Rename parent folder
    print("1. Renaming 'Grouped Brand Discovery' → 'Grouped Brand HQ'...")
    service.files().update(
        fileId=PARENT_FOLDER_ID,
        body={'name': 'Grouped Brand HQ'}
    ).execute()
    print("  ✓ Renamed!\n")

    # 2. Create missing top-level folders
    print("2. Creating folder structure...\n")

    folders = {
        'Brand Guide': None,          # Already exists
        'Visual Identity Assets': None, # Already exists
        'Competitive Analysis': None,  # Already exists
        'Archive': None,               # Already exists
        'Target Audience': None,       # NEW
        'Verbal Identity': None,       # NEW
        'Content Strategy': None,      # NEW
        'Social Media': None,          # NEW
        'GTM': None,                   # NEW
        'Product': None,               # NEW
        '_meta': None,                 # NEW
    }

    for name in folders:
        folders[name] = find_or_create_folder(service, name, PARENT_FOLDER_ID)

    # 3. Create subfolders
    print("\n3. Creating subfolders...\n")

    # Content Strategy subfolders
    find_or_create_folder(service, 'Campaigns', folders['Content Strategy'])

    # Social Media subfolders
    find_or_create_folder(service, 'Social Listening', folders['Social Media'])

    # Product subfolders
    find_or_create_folder(service, 'User Research', folders['Product'])

    print("\n✅ Done! Grouped Brand HQ folder structure is ready.")
    print(f"\n   📁 https://drive.google.com/drive/folders/{PARENT_FOLDER_ID}")


if __name__ == '__main__':
    main()
