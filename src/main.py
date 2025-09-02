from googleapiclient.discovery import build
from google.oauth2 import service_account

# Path to service account credentials
SERVICE_ACCOUNT_FILE = "credentials/databridge-service.json"

# Scopes = permissions for Docs + Drive
SCOPES = [
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

# Authenticate
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Build Docs API service
docs_service = build('docs', 'v1', credentials=creds)

# Replace with your Doc ID (from its URL)
DOCUMENT_ID = "YOUR_GOOGLE_DOC_ID_HERE"

doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
print("Title:", doc.get('title'))
