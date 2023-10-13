
# # from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

from flask import Flask
import requests

site = input('\nEnter link : ')
if site == '':
    site = 'https://github.com/imvickykumar999'

req = requests.get(site)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return req.text

if __name__ == '__main__':
    app.run(debug=False)
