import json
import os

from flask import Flask, render_template, jsonify

from displays import display_image, display_text, EInkRenderer, VirtualRenderer
import requests

app = Flask(__name__)

DISPLAY_TEXT = False

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

if ENVIRONMENT != "pi":
    renderer = EInkRenderer()
else:
    renderer = VirtualRenderer()

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
    ngrok_url = get_ngrok_url()  # TODO: replace with cloudflare tunnel
    return render_template("index.html", ngrok_url=ngrok_url)


def get_ngrok_url():
    # Get the ngrok tunnels info
    tunnels = requests.get("http://localhost:4040/api/tunnels").json()

    # Extract the public URL (assuming you have only one tunnel active)
    ngrok_url = tunnels['tunnels'][0]['public_url']

    return ngrok_url
