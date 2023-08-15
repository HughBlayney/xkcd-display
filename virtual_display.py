from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, jsonify

app = Flask(__name__)

IMAGE_PATH = "node_image_streamer/static/display.png"



text = "hello world"

# Create a new image with the provided text
image = Image.new('RGB', (300, 100), color=(73, 109, 137))
d = ImageDraw.Draw(image)
fnt = ImageFont.truetype("/Library/Fonts/Arial.ttf", 15)
d.text((10, 10), text, font=fnt, fill=(255, 255, 0))

# Save the image
image.save(IMAGE_PATH)


