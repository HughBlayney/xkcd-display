from waveshare_epd import epd7in5_V2
import os
from PIL import Image,ImageDraw,ImageFont
import time
import argparse

parser = argparse.ArgumentParser(description="Display an image on the e-Ink Display.")
parser.add_argument("--image-path", type=str, default="./comic.png")
parser.add_argument("--text", type=str, default=None)

def display_image(image_path: str="./comic.png", refresh_to_white: bool=True):
   epd = epd7in5_V2.EPD()
   epd.init()

   if refresh_to_white:
      print("Clear")
      epd.Clear()
      time.sleep(5)

   png = Image.open(image_path)
   epd.display(epd.getbuffer(png))

def display_text(text: str, refresh_to_white: bool=True):
   epd = epd7in5_V2.EPD()
   epd.init()

   xkcd_font = ImageFont.truetype("./font.ttf", 24)

   if refresh_to_white:
      print("Clear")
      epd.Clear()
      time.sleep(5)

   Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
   draw = ImageDraw.Draw(Himage)
   draw.text((2, 0), text, font = xkcd_font, fill = 0)
   epd.display(epd.getbuffer(Himage))
    

if __name__ == "__main__":
   args = parser.parse_args()
   if args.text is not None:
      display_text(args.text, refresh_to_white=False)
      time.sleep(10)
   display_image(args.image_path, refresh_to_white=False)