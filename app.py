import json

from decouple import config
from flask import Flask, render_template, jsonify

app = Flask(__name__)

DISPLAY_TEXT = False

XKCD_ENVIRONMENT = config("XKCD_ENVIRONMENT", default="pi")
XKCD_REMOTE_WEBSITE = config("XKCD_REMOTE_WEBSITE")

if XKCD_ENVIRONMENT != "pi":
    from renderers.virtual_renderer import VirtualRenderer as renderer
else:
    from renderers.eink_renderer import EInkRenderer as renderer

renderer = renderer()


@app.route("/flip")
def hello_world():
    global DISPLAY_TEXT
    if DISPLAY_TEXT:
        renderer.display_image()
        DISPLAY_TEXT = False
    else:
        alt = read_alt_text()
        renderer.display_text(alt)
        DISPLAY_TEXT = True
    return jsonify({"message": "Flip successful!"}), 200


def read_alt_text():
    with open("meta.json", "r") as metadata_file:
        metadata = json.load(metadata_file)
    return metadata["alt"]


@app.route("/")
def remote():
    return render_template("index.html")
