from flask import Flask

from display import display_image, display_text

app = Flask(__name__)

DISPLAY_TEXT = False


@app.route("/flip")
def hello_world():
    global DISPLAY_ALT_TEXT
    if DISPLAY_ALT_TEXT:
        display_image()
        DISPLAY_TEXT = False
    else:
        display_text()
        DISPLAY_TEXT = True
