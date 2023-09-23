
# https://pypi.org/project/VicksTor/
from flask import Flask, render_template
import os

from HostTor import VicksTor
import VicksTor

# template_dir = os.path.abspath('./')
app = Flask(
        __name__, 
        # template_folder=template_dir
    )

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
