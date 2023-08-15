import argparse
import json
from typing import Optional

import requests

parser = argparse.ArgumentParser()

parser.add_argument(
    "--comic-number",
    help=(
        "Integer comic number to get. "
        + "Leave blank for None, which fetches latest comic. "
        + "Enter a negative integer to get the latest-nth comic."
    ),
    type=int,
    default=None,
)

parser.add_argument(
    "--out-comic-filename",
    help="Filename to save comic image to. Defaults to 'comic.png'.",
    type=str,
    default="comic.png",
)

parser.add_argument(
    "--out-meta-filename",
    help="Filename to save comic metadata to. Defaults to 'meta.json'.",
    type=str,
    default="meta.json",
)

def get_comic_info_json(comic_number: Optional[int] = None) -> dict:
    if comic_number is None:
        info_url = "https://xkcd.com/info.0.json"
    else:
        if comic_number < 0:
            latest_comic_number = json.loads(
                requests.get("https://xkcd.com/info.0.json").text
            )["num"]
            info_url = (
                "https://xkcd.com/"
                + f"{latest_comic_number + comic_number}/info.0.json"
            )
        else:
            info_url = f"https://xkcd.com/{comic_number}/info.0.json"

    info_response = requests.get(info_url)

    info_json = json.loads(info_response.text)

    return info_json

def download_comic(
    comic_number: Optional[int] = None,
    out_comic_filename: str = "comic.png",
    out_meta_filename: str = "meta.json",
):
    """
    Downloads an xkcd comic and saves it to a file.
    """
    info_json = get_comic_info_json(comic_number=comic_number)

    comic_image = requests.get(info_json["img"])

    with open(out_comic_filename, "wb") as f:
        f.write(comic_image.content)
    
    with open(out_meta_filename, "w") as f:
        json.dump(info_json, f, indent=2)

if __name__ == "__main__":
    args = parser.parse_args()
    download_comic(
        comic_number=args.comic_number,
        out_comic_filename=args.out_comic_filename,
        out_meta_filename=args.out_meta_filename,
    )
