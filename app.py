from flask import Flask, make_response

app = Flask(__name__)

@app.route("/auth")
def authorize():
    resp = make_response()
    resp.headers["Location"] = "rtmp://172.20.0.3:1936/segmenter/colors"
    resp.status = 302
    return resp