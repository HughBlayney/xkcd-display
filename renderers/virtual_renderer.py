from random import random

from PIL import Image, ImageDraw, ImageFont
from decouple import config

from renderers.abstract_renderer import AbstractRenderer

IMAGE_PATH = config("XKCD_VIRTUAL_IMAGE_PATH")


class VirtualRenderer(AbstractRenderer):

    @staticmethod
    def display_image(image_path: str = "./resized.png", refresh_to_white: bool = True,
                      flip_vertical: bool = True):
        print("displaying image at path: " + image_path)

    @staticmethod
    def display_text(text: str, refresh_to_white: bool = True, flip_vertical: bool = True):
        text = f"hello world foo + {random()}"
        # Create a new image with the provided text
        image = Image.new('RGB', (480, 800), color=(73, 109, 137))
        d = ImageDraw.Draw(image)
        fnt = ImageFont.truetype("/Library/Fonts/Arial.ttf", 15)
        d.text((10, 10), text, font=fnt, fill=(255, 255, 0))

        # Save the image
        image.save(IMAGE_PATH)

        print("displaying text at path: " + text)
