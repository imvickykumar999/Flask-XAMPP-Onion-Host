
# from HostTor import VicksTor
# import VicksTor

from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a href="/Instagram Reels">Index of</a>'

@app.route('/Instagram Reels/<path:filename>')
def send_vixtify(filename):
    return send_from_directory(".", filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
