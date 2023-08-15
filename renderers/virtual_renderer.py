from random import random

from PIL import Image, ImageDraw, ImageFont

from renderers.abstract_renderer import AbstractRenderer


class VirtualRenderer(AbstractRenderer):

    def display_image(self, image_path: str = "./resized.png", refresh_to_white: bool = True,
                      flip_vertical: bool = True):
        print("displaying image at path: " + image_path)

    def display_text(self, text: str, refresh_to_white: bool = True, flip_vertical: bool = True):
        image_path = "node_image_streamer/static/display.png"
        text = f"hello world foo + {random()}"
        # Create a new image with the provided text
        image = Image.new('RGB', (300, 100), color=(73, 109, 137))
        d = ImageDraw.Draw(image)
        fnt = ImageFont.truetype("/Library/Fonts/Arial.ttf", 15)
        d.text((10, 10), text, font=fnt, fill=(255, 255, 0))

        # Save the image
        image.save(image_path)

        print("displaying text at path: " + text)
