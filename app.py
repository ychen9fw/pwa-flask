import build
from flask import Flask, request
app = Flask(__name__)


@app.route('/build_apk', methods=['POST'])
def build_apk():
    content = request.json
    result = build.build(content['website'])
    return 'Build: ' + result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

