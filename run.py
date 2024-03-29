import json
import subprocess

from display_drivers.eink import EInkDisplayDriver
from download_comic import download_comic, get_comic_info_json

if __name__ == "__main__":
    try:
        with open("data/meta.json") as f:
            meta = json.load(f)
        displayed_comic_number = meta.get("num", None)
    except FileNotFoundError:
        displayed_comic_number = None

    latest_comic_info_json = get_comic_info_json()

    latest_comic_number = latest_comic_info_json.get("num", None)

    if latest_comic_number is None or latest_comic_number == displayed_comic_number:
        print("No new comic to display")
    else:
        download_comic()
        subprocess.run(
            [
                "convert",
                "data/comic.png",
                "-resize",
                "800x480",
                "-background",
                "white",
                "-gravity",
                "center",
                "-extent",
                "800x480",
                "resized.png",
            ]
        )
        EInkDisplayDriver.display_image()
