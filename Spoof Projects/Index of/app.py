
# # from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('xampp')

# --------------------------------

# # from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

from flask import (
    Flask,
    render_template, 
    send_from_directory
)

import os
app = Flask(__name__, template_folder='./')
path = 'Reels'

@app.route(f'/{path}/<path:filename>')  
def send_file(filename):
    return send_from_directory(f'./{path}', filename)

@app.route(f'/index_files/<path:filename>')  
def index_files(filename):
    return send_from_directory(f'./index_files', filename)

@app.route('/')
def hello_world():
    files = os.listdir(f'./{path}')
    return render_template(
        'index.html', 
        files=files, 
        path=path,
    )

if __name__ == '__main__':
    app.run(debug = 1)
