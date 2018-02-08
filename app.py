from flask import Flask, jsonify, request
from datetime import *
import socket
import pprint

app = Flask(__name__)


def getNetworkIp(site='google.com'):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((site, 0))
    return s.getsockname()[0]


@app.route('/')
def app_route__():
    return jsonify(
      Date=datetime.now(),
      HostName=socket.gethostname(),
      Message='Hello World from Docker!',
      MyIP=getNetworkIp(),
      YourIP=request.remote_addr,
      ForwardedFor=request.headers.getlist('X-Forwarded-For')
    )


@app.route('/request')
def app_route__request():
    return jsonify(
      Date=datetime.now(),
      HostName=socket.gethostname(),
      MyIP=getNetworkIp(),
      YourIP=request.remote_addr,
      Request=pprint.pformat(request.__dict__)
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
