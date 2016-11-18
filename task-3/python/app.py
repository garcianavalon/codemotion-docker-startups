import socket

from flask import Flask
from flask import render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
 hits = redis.incr('hits')
 hostname = socket.gethostname()
 return render_template('index.html', hostname=hostname, hits=hits)


if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True)
