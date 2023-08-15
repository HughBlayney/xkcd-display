# abstract
import abc
from abc import ABC

from PIL import Image, ImageDraw, ImageFont


class AbstractTextRenderer(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abc.abstractmethod
    def render(self, text: str) -> Image:
        raise NotImplementedError


class XKCDAltTextRenderer(AbstractTextRenderer):
    xkcd_font = ImageFont.truetype("./font.ttf", 24)

    def render(self, text: str) -> Image:
        # Center the text
        image = Image.new("1", (self.width, self.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        w, h = draw.textsize(text, font=self.xkcd_font)
        # Move the text onto multiple lines if it is too long
        if w > self.width:
            words = text.split()
            lines = []
            line = ""
            for word in words:
                if draw.textsize(line + word, font=self.xkcd_font)[0] < self.width:
                    line += word + " "
                else:
                    lines.append(line)
                    line = word + " "
            lines.append(line)
            text = "\n".join(lines)
            w, h = draw.textsize(text, font=self.xkcd_font)
        draw.text(((self.width - w) / 2, (self.height - h) / 2), text, font=self.xkcd_font, fill=0)
