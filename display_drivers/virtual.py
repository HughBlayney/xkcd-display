from PIL import Image
from decouple import config

from display_drivers.abstract import AbstractDisplayDriver, EPD480x800
from renderers.xkcd_alt_text_renderer import XKCDAltTextRenderer

IMAGE_PATH = config("XKCD_VIRTUAL_IMAGE_PATH")


class VirtualDisplayDriver(AbstractDisplayDriver, EPD480x800):
    path = IMAGE_PATH

    def display(self, image: Image):
        image.save(self.path)

    def display_image(self, image_path: str = "./resized.png"):
        image = Image.open(image_path)
        self.display(image)
        print("displaying image at path: " + image_path)

    def display_text(self, text: str):
        image = XKCDAltTextRenderer(width=self.width, height=self.height).render(text)
        self.display(image)
        print("displaying text at path: " + text)
