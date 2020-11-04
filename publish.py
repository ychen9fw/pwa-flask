import requests
import json


def publish(cid, secret, aid):
    outcome = "success"
    url = "https://connect-api.cloud.huawei.com/api/oauth2/v1/token"
    payload = "{\"grant_type\":\"client_credentials\"," \
              "\"client_id\":\"%s\"," \
              "\"client_secret\":\"%s\"}"\
              % (cid, secret)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
    token = json.loads(response.text)['access_token']
    url = "https://connect-api.cloud.huawei.com/api/publish/v2/upload-url"
    headers = {
        'Content-Type': 'application/json',
        'client_id': cid,
        'Authorization': 'Bearer ' + token
    }
    query = {
        'appId': aid,
        'suffix': 'apk'
    }
    response = requests.request("GET", url, headers=headers, params=query)
    print(response.text.encode('utf8'))
    uploadUrl = json.loads(response.text)['uploadUrl']
    chunkUploadUrl = json.loads(response.text)['chunkUploadUrl']
    authCode = json.loads(response.text)['authCode']
    return outcome

if __name__ == "__main__":
    publish("487884425208530048",
            "92F4F51BB5D1C6ADA913E9333898F02463E66D1C8DBCD6937C694E638B973DAC",
            "103201705")
