
# https://jordan-wright.com/blog/2014/10/06/creating-tor-hidden-services-with-python/

# First open tor browser,
# then run this file

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    from stem.control import Controller
    
    port = 5000
    host = "127.0.0.1"
    hidden_svc_dir = "C:/Users/Vicky/Desktop/Repository/Host-Onion/Tor Browser/HiddenService/flask_app"

    print (" * Getting controller")
    controller = Controller.from_port(address=host, port=9151)

    try:
        controller.authenticate(password="")
        controller.set_options([
            ("HiddenServiceDir", hidden_svc_dir),
            ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
            ])
        svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
        print (" * Created host: %s" % svc_name)

    except Exception as e:
        print (e)

    app.run(
        host="0.0.0.0", 
        debug=True
    )
