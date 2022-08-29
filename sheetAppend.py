import requests

def handler(pd: "pipedream"):

  authorization = f'Bearer {pd.inputs["google_sheets"]["$auth"]["oauth_access_token"]}'
  headers = {"Authorization": authorization}

  spreadsheetId = '1abcd0eFgYoBcs59vbx8hseeZuwPgi3xL7VMu1802t1g';

  data = {
    "range": "test",
    "values": [
      list(pd.steps["Order_confirmation"]["$return_value"]["Name"].values()),
      list(pd.steps["Order_confirmation"]["$return_value"]["Currency"].values()),
      list(pd.steps["Order_confirmation"]["$return_value"]["Total"].values()),
      list(pd.steps["Order_confirmation"]["$return_value"]["Payment Method"].values()),
      list(pd.steps["Order_confirmation"]["$return_value"]["Source"].values())
    ],
    "majorDimension": "COLUMNS",
  }

  params = {
    "alt": "json",
    "valueInputOption": "RAW"
  }

  r = requests.post(
    f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/test:append',
    headers=headers,
    json=data,
    params=params
  );
  
  return r.json();
