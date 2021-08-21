from flask import Flask, make_response

app = Flask(__name__)

@app.route("/auth")
def authorize():
    resp = make_response()
    resp.headers["Location"] = "rtmp://127.0.0.1:1935/pusher/colors"
    resp.status = 302
    return resp