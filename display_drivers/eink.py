# abstract
import abc
import time
from abc import ABC

from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd7in5_V2_fast as epd7in5_V2

from display_drivers.abstract import AbstractDisplayDriver, EPD480x800
from renderers.xkcd_alt_text_renderer import XKCDAltTextRenderer


class EInkDisplayDriver(AbstractDisplayDriver, EPD480x800):
    def display_image(self, image_path: str = "./resized.png"):
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()
        time.sleep(1)
        png = Image.open(image_path)
        png = png.transpose(Image.ROTATE_180)
        epd.display(epd.getbuffer(png))

    def display_text(self, text: str):
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()
        time.sleep(1)
        image = XKCDAltTextRenderer(self.width, sel).render(text)
        image = image.transpose(Image.ROTATE_180)
        epd.display(epd.getbuffer(image))

