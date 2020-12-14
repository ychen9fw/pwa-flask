import build
import publish
import time
import os
import base64
from flask_cors import CORS
from flask import Flask, request, send_file, send_from_directory, safe_join, abort
import logging

app = Flask(__name__)
CORS(app)


@app.route('/build_apk', methods=['POST'])
def build_apk():
    content = request.json
    print(content)
    print(content['agcs'])
    folder = build.build(content['packageId'],
                         content['host'],
                         content.get('HMSKits', ''),
                         content['ads_id'],
                         content['agcs'].replace('data:application/json;base64,', ''),
                         content['signing']['alias'],
                         content['signing']['fullName'],
                         content['signing']['organization'],
                         content['signing']['organizationalUnit'],
                         content['signing']['countryCode'],
                         content['signing']['keyPassword'],
                         content['signing']['storePassword'],
                         content.get('iconUrl', '')
                         )
    # return 'Build: ' + result
    print('returning folder' + folder)
    return send_from_directory(folder, filename="pwa.zip", as_attachment=True, mimetype='application/zip')


@app.route('/publish_apk', methods=['POST'])
def publish_apk():
    content = request.json
    print(content)
    folder = str("/tmp/pwa_apk"+str(int(time.time()*1000)))
    os.system("mkdir " + folder)
    file = open(folder + '/pwa.apk', 'wb')
    file.write(base64.b64decode(content['apk'].replace('data:application/vnd.android.package-archive;base64,', '')))
    file.close()
    outcome = publish.publish(content['client_id'], content['client_key'], content['app_id'], folder + "/pwa.apk")
    return outcome


@app.route('/', methods=['GET'])
def get_success():
    return 'get success'


if __name__ == "__main__":
    logging.basicConfig(filename='/home/ubuntu/api_error.log',level=logging.DEBUG)
    app.run(host="0.0.0.0", port=80)

