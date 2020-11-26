import build
import publish
import time
import os
from flask_cors import CORS
from flask import Flask, request, send_file, send_from_directory, safe_join, abort

app = Flask(__name__)
CORS(app)

@app.route('/build_apk', methods=['POST'])
def build_apk():
    content = request.json
    print(content)
    print(content['agcs'])
    folder = build.build(content['packageId'],
                         content['host'],
                         content['HMSKits'],
                         content['ads_id'],
                         content['agcs'].replace('data:application/json;base64,', ''),
                         content['signing']['alias'],
                         content['signing']['fullName'],
                         content['signing']['organization'],
                         content['signing']['organizationalUnit'],
                         content['signing']['countryCode'],
                         content['signing']['keyPassword'],
                         content['signing']['storePassword'],
                         content['iconUrl']
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
    os.system("echo " + content['apk'] + " | base64 --decode > " + folder + "/pwa.apk")
    outcome = publish.publish(content['client_id'], content['client_key'], content['app_id'], folder + "/pwa.apk")
    return outcome


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

