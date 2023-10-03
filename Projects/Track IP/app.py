
# https://stackoverflow.com/a/3760309/11493297

import socket
from flask import Flask
# from HostTor import VicksTor
import VicksTor

VicksTor.run_server('flask')
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return f'''
<meta http-equiv="refresh" content="3; URL=/">
hostname : {hostname}
<br>
ip_address : {ip_address}
''', 200

if __name__ == '__main__':
    app.run()
