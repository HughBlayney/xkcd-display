from pathlib import Path


import json

import requests


result = requests.get("https://xkcd.com/info.0.json")

"""
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

result_json = json.loads(result.text)

result = requests.get(result_json["img"])

with open(Path(__file__).parent / "comic.png", "wb") as f:
    f.write(result.content)

