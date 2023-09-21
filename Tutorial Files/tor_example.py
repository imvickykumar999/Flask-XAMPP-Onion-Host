# https://jordan-wright.com/blog/2014/10/06/creating-tor-hidden-services-with-python/

# First open tor browser,
# then run this file

from stem.control import Controller
from flask import Flask

if __name__ == "__main__":
    app = Flask("__name__")

    port = 5000
    host = "127.0.0.1"
    hidden_svc_dir = "C:/Users/Vicky/Desktop/Repository/Host-Onion/Tor Browser/tor_example"

    @app.route('/')
    def index():
        return "<h1>Tor works!</h1>"
    
    print (" * Getting controller")
    controller = Controller.from_port(address="127.0.0.1", port=9151)

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
    app.run()
