import requests
import json


def publish(cid, secret, aid, apk):
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
    headers = {
        # 'Content-Type': 'application/json',
        'accept': 'application/json'
    }
    multipart_form_data = {
        'file': ('pwa.apk', open(apk, 'rb')),
        'authCode': (None, authCode),
        'fileCount': (None, '1')
    }
    response = requests.request("POST", uploadUrl, files=multipart_form_data, headers=headers,)
    print(response.text.encode('utf8'))
    fileurl = json.loads(response.text)['result']['UploadFileRsp']['fileInfoList'][0]['fileDestUlr']

    url = "https://connect-api.cloud.huawei.com/api/publish/v2/app-file-info"
    headers = {
        'Content-Type': 'application/json',
        'client_id': cid,
        'Authorization': 'Bearer ' + token
    }
    query = {
        'appId': aid
    }
    payload = json.dumps({"fileType": 5, "files": [{"fileName": "pwa.apk", "fileDestUrl": fileurl}]})
    response = requests.request("PUT", url, headers=headers, params=query, data=payload)
    print(response.text.encode('utf8'))

    return response.text.encode('utf8')


if __name__ == "__main__":
    publish("487884425208530048",
            "92F4F51BB5D1C6ADA913E9333898F02463E66D1C8DBCD6937C694E638B973DAC",
            "103238465",
            "pwa.apk")
