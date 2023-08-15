from random import random

from decouple import config

from display_drivers.abstract import AbstractDisplayDriver, EPD480x800
from renderers.xkcd_alt_text_renderer import XKCDAltTextRenderer

IMAGE_PATH = config("XKCD_VIRTUAL_IMAGE_PATH")


class VirtualDisplayDriver(AbstractDisplayDriver, EPD480x800):

    def display_image(self, image_path: str = "./resized.png"):
        print("displaying image at path: " + image_path)

    def display_text(self, text: str):
        text = f"hello world foo + {random()}"

        image = XKCDAltTextRenderer(width=self.width, height=self.height).render(text)
        # Save the image
        image.save(IMAGE_PATH)

        print("displaying text at path: " + text)
