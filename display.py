import argparse
import json
import time

from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd7in5_V2_fast as epd7in5_V2

parser = argparse.ArgumentParser(description="Display an image on the e-Ink Display.")
image_or_text_group = parser.add_mutually_exclusive_group(required=True)
image_or_text_group.add_argument(
    "--comic",
    help="Display the comic on the e-Ink Display.",
    action="store_true",
)
image_or_text_group.add_argument(
    "--alt-text",
    help="Display the alt-text on the e-Ink Display.",
    action="store_true",
)
parser.add_argument(
    "--image-filename",
    help="The filename of the image to display.",
    type=str,
    default="resized.png",
)
parser.add_argument(
    "--metadata-filename",
    help="The filename of the metadata file from which to get the alt-text.",
    type=str,
    default="meta.json",
)


def display_image(image_path: str = "./comic.png", refresh_to_white: bool = True):
    epd = epd7in5_V2.EPD()
    epd.init()

    if refresh_to_white:
        print("Clear")
        epd.Clear()
        time.sleep(1)

    png = Image.open(image_path)
    epd.display(epd.getbuffer(png))


def display_text(text: str, refresh_to_white: bool = True):
    epd = epd7in5_V2.EPD()
    epd.init()

    xkcd_font = ImageFont.truetype("./font.ttf", 24)

    if refresh_to_white:
        print("Clear")
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
    epd.display(epd.getbuffer(Himage))


if __name__ == "__main__":
    args = parser.parse_args()
    if args.comic:
        display_image(args.image_filename)
    else:
        with open(args.metadata_filename, "r") as metadata_file:
            metadata = json.load(metadata_file)
        display_text(metadata["alt"])
