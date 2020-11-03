import requests

url = "https://connect-api.cloud.huawei.com/api/oauth2/v1/token"

payload = "{   \r\n    \"grant_type\":\"client_credentials\",   \r\n    \"client_id\":\"487884425208530048\",   \r\n    \"client_secret\":\"92F4F51BB5D1C6ADA913E9333898F02463E66D1C8DBCD6937C694E638B973DAC\"\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
