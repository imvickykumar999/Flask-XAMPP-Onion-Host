
# from HostTor import VicksTor
# import VicksTor
# VicksTor.run_server('flask')

import cv2
from flask import (
    Flask, 
    render_template, 
    Response
)

app = Flask(__name__)
ip = '192.168.0.101'
port = '8080'

username = 'imvickykumar999'
password = 'imvickykumar999'
camera = cv2.VideoCapture(f'http://{username}:{password}@{ip}:{port}/video')

# # # http://80.32.125.254:8080/cgi-bin/guestimage.html
# ip = '80.32.125.254'
# port = '8080'

# camera = cv2.VideoCapture(f'http://{ip}:{port}') # no authentication
# camera = cv2.VideoCapture(0) # laptop webcam

def generate_frames():
    while True:
        # camera = cv2.VideoCapture(f'http://{ip}:{port}/record/current.jpg')

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__=="__main__":
    app.run(debug=False)


'''
# [mjpeg @ 000001c4ed7b5340] overread 8
# [http @ 000001c4ed85cf40] Stream ends prematurely at 7325, should be 104197

Here are some possible solutions to the error "Stream ends prematurely at 7325, should be 104879":
Check your RAM storage. The device may not have enough RAM.
Decouple the input reading and processing sides of your code by sticking a queue in the middle.
Make your chunk size smaller and do less processing.
Check your network or server. The network or server may not be reliable.
Check the htop to see RAM storage. The device may not have enough RAM.
'''
