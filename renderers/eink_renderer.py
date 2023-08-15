# abstract

import time

from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd7in5_V2_fast as epd7in5_V2

from renderers.abstract_renderer import AbstractRenderer


class EInkRenderer(AbstractRenderer):
    def display_image(image_path: str = "./resized.png", refresh_to_white: bool = True, flip_vertical: bool = True):
        epd = epd7in5_V2.EPD()
        epd.init()

        if refresh_to_white:
            epd.Clear()
            time.sleep(1)

        png = Image.open(image_path)
        if flip_vertical:
            png = png.transpose(Image.ROTATE_180)
        epd.display(epd.getbuffer(png))

    def display_text(text: str, refresh_to_white: bool = True, flip_vertical: bool = True):
        epd = epd7in5_V2.EPD()
        epd.init()

        xkcd_font = ImageFont.truetype("./font.ttf", 24)

        if refresh_to_white:
            epd.Clear()
            time.sleep(1)
        # Center the text
        Himage = Image.new("1", (epd.width, epd.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        w, h = draw.textsize(text, font=xkcd_font)
        # Move the text onto multiple lines if it is too long
        if w > epd.width:
            words = text.split()
            lines = []
            line = ""
            for word in words:
                if draw.textsize(line + word, font=xkcd_font)[0] < epd.width:
                    line += word + " "
                else:
                    lines.append(line)
                    line = word + " "
            lines.append(line)
            text = "\n".join(lines)
            w, h = draw.textsize(text, font=xkcd_font)
        draw.text(((epd.width - w) / 2, (epd.height - h) / 2), text, font=xkcd_font, fill=0)
        if flip_vertical:
            Himage = Himage.transpose(Image.ROTATE_180)
        epd.display(epd.getbuffer(Himage))
