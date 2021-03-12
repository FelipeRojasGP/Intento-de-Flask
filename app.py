from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template , stream_with_context
from gevent.pywsgi import WSGIServer
import json
import time

app = Flask(__name__)
counter = 100

##############################
@app.route("/")
def render_index():
  return render_template("index.html")

##############################
@app.route("/hello",methods=["GET", "POST"])
def hello():
    return flask.Response(event_stream(), mimetype="text/event-stream")

def event_stream():
  return "hello"
        
##############################
if __name__ == "__main__":
  # app.run(port=80, debug=True)
  http_server = WSGIServer(("localhost", 80), app)
  http_server.serve_forever() 








