
# # from HostTor import VicksTor
# import VicksTor
# VicksTor.run_server('flask')

from flask import (
    Flask, 
    request, 
    render_template, 
    send_from_directory
)
app = Flask(__name__, template_folder='./')

@app.route('/', methods=['POST'])
def login():
    return render_template('index.html')

@app.route('/<path:filename>')  
def send_file(filename):
    return send_from_directory('./', filename)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = False)