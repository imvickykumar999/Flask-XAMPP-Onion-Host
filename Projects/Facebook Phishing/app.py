
# from HostTor import VicksTor
import VicksTor
VicksTor.run_server('flask')

from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/templates/Facebook_files/<path:filename>')  
def send_file(filename):
    return send_from_directory('./templates/Facebook_files', filename)

@app.route('/')
def hello_world():
    return render_template('Facebook.html')

if __name__ == '__main__':
    app.run()
