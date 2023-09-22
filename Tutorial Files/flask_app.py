
from flask import Flask
from HostTor import VicksTor
import VicksTor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! <br> I am Anonumous.'

if __name__ == '__main__':
    app.run()
