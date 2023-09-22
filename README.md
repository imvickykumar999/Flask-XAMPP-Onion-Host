># `Host Flask on Tor using pip`
>
>![image](https://github.com/imvickykumar999/Flask-XAMPP-Onion-Host/assets/50515418/0e6c3d47-8930-414a-af6b-ad49d62e5d85)

<br>

## 🫡 `Use my` `VicksTor Library`

```python
from flask import Flask

# https://pypi.org/project/VicksTor/
from HostTor import VicksTor
import VicksTor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! <br> I am Anonumous.'

if __name__ == '__main__':
    app.run()
```

<br>

![image](https://github.com/imvickykumar999/Flask-XAMPP-Onion-Host/assets/50515418/137a55a7-bfe9-4304-a385-2a51b0c10cdd)

<br>

# `Steps to Host on Tor Manually`

    Fun Fact: 
        onion sites are hosted locally on your device (Laptop, Raspberry Pi, etc.)

<br>

## `for static deployment`
    
    torrc: 
        \Tor Browser\Browser\TorBrowser\Data\Tor\
    
    HiddenServiceDir C:\Users\Vicky\Desktop\Repository\Host-Onion\Tor Browser\HiddenService\static_folder
    HiddenServicePort 80 127.0.0.1

    index.html
        (add html files here):
            \xampp\htdocs
            
    Run Server:
        XAMPP Control Panel 
            
            Module: Apache
            Action: Start

    Start Tor Browser (.shortcut):
        (files will be generated at)
            \Tor Browser\HiddenService\static_folder
            
    hostname (Tor link generated):
        i5hfkdpxlqjbojuiqt242h5vtgvic7jyzkfkj5ttdcatwycudprl74qd.onion

    access.log (optional, see real-time logs): 
        C:\xampp\apache\logs

    To down the site:
        XAMPP Control Panel:
    
            Module: Apache
            Action: Stop

<br>

## `for flask deployment`

    torrc: 
        \Tor Browser\Browser\TorBrowser\Data\Tor\
    
    HiddenServiceDir C:\Users\Vicky\Desktop\Repository\Host-Onion\Tor Browser\HiddenService\flask_app
    HiddenServicePort 80 127.0.0.1:9151

    Start Tor Browser (.shortcut):
        (files will be generated at)
            \Tor Browser\HiddenService\flask_app
            
    Run Server:
        python flask_app.py
    
            http://127.0.0.1/
            or,
            localhost

    hostname (Tor link generated):
        ikruscfbjtf7zcd2dvxfoiqzl4aqqorudxmf22jhrhnxjb24e2mdieqd.onion

    access logs and errors:
        (in CMD)

    To down the site:
        Ctrl+C in CMD Server
        Close Tor Browser

<br>

## `flask_app.py`

> First open tor browser, then run below file.

<br>

    >>> python flask_app.py

```python
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
```
