python download_comic.py
convert _data/comic.png -resize 800x480 -background white -gravity center -extent 800x480 _data/resized.png
python display.py --comic
