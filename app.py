import json
import subprocess
from random import random

from decouple import config
from flask import Flask, render_template, jsonify

from download_comic import get_comic_info_json, download_comic

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
def random_comic():
    number = get_comic_info_json()["num"]
    print("number: " + str(number))
    random_comic_number = int(random() * number)
    print("random_comic_number: " + str(random_comic_number))
    download_comic(comic_number=random_comic_number, out_comic_filename="data/comic.png")
    resize("data/comic.png", "data/resized.png")
    display_driver.display_image("data/resized.png")
    return jsonify({"message": "Random comic successful!"}), 200


def resize(input_path: str, output_path: str):
    subprocess.run(
        [
            "convert",
            input_path,
            "-resize",
            "800x480",
            "-background",
            "white",
            "-gravity",
            "center",
            "-extent",
            "800x480",
            output_path,
        ]
    )


def read_alt_text():
    print("hello")
    with open("data/meta.json", "r") as metadata_file:
        metadata = json.load(metadata_file)
    return metadata["alt"]


@app.route("/")
def remote():
    return render_template("index.html")
