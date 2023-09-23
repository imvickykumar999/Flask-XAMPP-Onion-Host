
from flask import Flask
app = Flask(__name__)

# https://pypi.org/project/VicksTor/
from HostTor import VicksTor
import VicksTor

@app.route('/')
def hello_world():
    return 'Hello, World! <br> I am Anonumous.'

if __name__ == '__main__':
    app.run(debug=False)

r'''
Microsoft Windows [Version 10.0.22631.2338]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Vicky\Desktop\Repository\Host-Onion\Tutorial Files>python fpython flask_app.py
Enter installed path of Tor Browser : C:\Users\Vicky\Desktop\Repository\Host-Onion\Tor Browser
 * Getting controller
 * Created host: phm3qet7n2fp4on2qq5l4e3vea5po4yrypa3slou6russpzbjl5hikyd.onion
 * Serving Flask app 'flask_app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [22/Sep/2023 22:03:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Sep/2023 22:03:21] "GET /favicon.ico HTTP/1.1" 404 -

C:\Users\Vicky\Desktop\Repository\Host-Onion\Tutorial Files>
'''
