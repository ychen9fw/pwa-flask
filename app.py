import build
from flask import Flask, request, send_file, send_from_directory, safe_join, abort

app = Flask(__name__)


@app.route('/build_apk', methods=['POST'])
def build_apk():
    content = request.json
    folder = build.build(content['website'])
    # return 'Build: ' + result
    return send_from_directory(folder, filename="pwa.zip", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

