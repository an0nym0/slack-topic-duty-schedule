# [START sheets_quickstart]
from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1wdLpDLMIS-v3XS1Fu3yS882LTf5DQ8M1ibcgD3DifQg'
# SAMPLE_RANGE_NAME = 'Current Schedule!B11:G17'
SAMPLE_RANGE_NAME = 'test!A2:H9'
SERVICE_ACCOUNT_FILE = 'credentials.json'

def main():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Duty:')
        for row in values:
            # Print columns from B to G, which correspond to indices from 0 to 5.
            print('%s, %s, %s, %s, %s, %s, %s, %s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
# [END sheets_quickstart]
