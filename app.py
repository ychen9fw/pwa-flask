import build
import publish
import time
import os
from flask import Flask, request, send_file, send_from_directory, safe_join, abort

app = Flask(__name__)


@app.route('/build_apk', methods=['POST'])
def build_apk():
    content = request.json
    print(content)
    folder = build.build(content['website'], content['HMSKits'], content['ads_id'], content['agcs'])
    # return 'Build: ' + result
    return send_from_directory(folder, filename="pwa.zip", as_attachment=True)


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

