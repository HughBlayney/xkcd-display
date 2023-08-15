import json

from decouple import config
from flask import Flask, render_template, jsonify

app = Flask(__name__)

DISPLAY_TEXT = False

XKCD_ENVIRONMENT = config("XKCD_ENVIRONMENT", default="pi")
XKCD_REMOTE_WEBSITE = config("XKCD_REMOTE_WEBSITE")

if XKCD_ENVIRONMENT != "pi":
    from display_drivers.virtual import VirtualDisplayDriver as DisplayDriver
else:
    from display_drivers.eink import EInkDisplayDriver as DisplayDriver

display_driver = DisplayDriver()


@app.route("/flip")
def flip():
    global DISPLAY_TEXT
    if DISPLAY_TEXT:
        display_driver.display_image()
        DISPLAY_TEXT = False
    else:
        alt = read_alt_text()
        display_driver.display_text(alt)
        DISPLAY_TEXT = True
    return jsonify({"message": "Flip successful!"}), 200

@app.route("/random")
def random():




def read_alt_text():
    with open("meta.json", "r") as metadata_file:
        metadata = json.load(metadata_file)
    return metadata["alt"]


@app.route("/")
def remote():
    return render_template("index.html")


