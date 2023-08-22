python download_comic.py
convert data/comic.png -resize 800x480 -background white -gravity center -extent 800x480 data/resized.png
python display.py --comic
