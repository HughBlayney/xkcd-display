from flask import Flask, render_template

from display import display_image, display_text

app = Flask(__name__)

DISPLAY_TEXT = False


@app.route("/flip")
def hello_world():
    global DISPLAY_TEXT
    if DISPLAY_TEXT:
        display_image()
        DISPLAY_TEXT = False
    else:
        display_text("hello world")
        DISPLAY_TEXT = True


@app.route("/")
def index():
    return render_template("index.html")
