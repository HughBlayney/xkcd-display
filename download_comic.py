import argparse
import json
from pathlib import Path
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
    type=Optional[int],
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

if __name__ == "__main__":
    args = parser.parse_args()
    """
    Result looks like:
    {
      "month": "10",
      "num": 2688,
      "link": "",
      "year": "2022",
      "news": "",
      "safe_title": "Bubble Universes",
      "transcript": "",
      "alt": "The theory finally unifies cosmic inflation and regular inflation.",
      "img": "https://imgs.xkcd.com/comics/bubble_universes.png",
      "title": "Bubble Universes",
      "day": "21"
    }
    """
    if args.comic_number is None:
        info_url = "https://xkcd.com/info.0.json"
    elif args.comic_number < 0:
        latest_comic_number = json.loads(
            requests.get("https://xkcd.com/info.0.json").text
        )["num"]
        info_url = (
            "https://xkcd.com/"
            + f"{latest_comic_number + args.comic_number}/info.0.json"
        )
    else:
        info_url = f"https://xkcd.com/{args.comic_number}/info.0.json"

    info_response = requests.get(info_url)

    info_json = json.loads(info_response.text)

    comic_image = requests.get(info_json["img"])

    with open(Path(__file__).parent / args.out_comic_filename, "wb") as f:
        f.write(comic_image.content)
    
    with open(Path(__file__).parent / args.out_meta_filename, "w") as f:
        json.dump(info_json, f, indent=2)
