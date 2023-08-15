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
    xkcd_prefix = "https://xkcd.com/"
    xkcd_suffix = "/info.0.json"

    first_comic_url = xkcd_prefix + xkcd_suffix
    first_comic_metadata = requests.get(first_comic_url)
    info_json = json.loads(first_comic_metadata.text)
    latest_comic_number = info_json["num"]

    # If comic_number is negative, we use modulo arithmetic to get the latest-nth comic
    comic_number = (latest_comic_number + comic_number) % latest_comic_number if comic_number else ''
    info_url = f"{xkcd_prefix}{comic_number}{xkcd_suffix}"

    return json.loads(requests.get(info_url).text)


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
