
# https://stackoverflow.com/a/3760309/11493297

from flask import request, Flask
# from HostTor import VicksTor
# import VicksTor

# VicksTor.run_server('flask')
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return f'''
<meta http-equiv="refresh" content="3; URL=/">
{request.remote_addr}
''', 200

if __name__ == '__main__':
    app.run()
