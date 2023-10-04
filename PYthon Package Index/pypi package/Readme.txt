
https://raw.githubusercontent.com/imvickykumar999/Flask-XAMPP-Onion-Host/main/Tutorial%20Files/VicksTor.py

# just add below 3 lines on top of app.py

from HostTor import VicksTor

import VicksTor as vix

vix.run_server('flask') # to run flask server

# vix.run_server('xampp') # to run apache server
