import time

from PIL import Image
from waveshare_epd import epd7in5_V2_fast as epd7in5_V2

from display_drivers.abstract import AbstractDisplayDriver, EPD480x800
from renderers.xkcd_alt_text_renderer import XKCDAltTextRenderer


class EInkDisplayDriver(AbstractDisplayDriver, EPD480x800):
    def __init__(self):
        self.epd = epd7in5_V2.EPD()
        self.epd.init()

    def display(self, image: Image):
        self.epd.Clear()
        time.sleep(1)
        image = image.transpose(Image.ROTATE_180)
        self.epd.display(self.epd.getbuffer(image))

    def display_image(self, image_path: str = "_data/resized.png"):
        png = Image.open(image_path)
        self.display(png)

    def display_text(self, text: str):
        image = XKCDAltTextRenderer(width=self.width, height=self.height).render(text)
        self.display(image)
