import requests

def handler(pd: "pipedream"):

  authorization = f'Bearer {pd.inputs["google_sheets"]["$auth"]["oauth_access_token"]}'
  headers = {"Authorization": authorization}

  spreadsheetId = '1abcd0eFgYoBcs59vbx8hseeZuwPgi3xL7VMu1802t1g';

  data = {
    'requests': [{
        "updateCells": {
            "range": {
                "sheetId": 123456789,
                "startRowIndex": 0,
                "startColumnIndex": 0
            },
            "rows": [
                {
                    "values": [
                        {
                            "userEnteredValue": {
                                "stringValue": "asaas"
                            }
                        },
                        {
                            "userEnteredValue": {
                                "stringValue": "sdsdsd"
                            }
                        }
                    ]
                },
                {
                    "values": [
                        {
                            "userEnteredValue": {
                                "stringValue": "ggg"
                            }
                        }
                    ]
                }
            ],
            "fields": "userEnteredFormat.textFormat,userEnteredValue"
        }
    }]
  }

  r = requests.post(
    f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}:batchUpdate?alt=json',
    headers=headers,
    json=data
  );
  
  return r.json();
