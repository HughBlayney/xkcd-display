import argparse
import json

from renderers.eink_renderer import EInkRenderer

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

if __name__ == "__main__":
    args = parser.parse_args()
    if args.comic:
        EInkRenderer.display_image(args.image_filename)
    else:
        with open(args.metadata_filename, "r") as metadata_file:
            metadata = json.load(metadata_file)
        EInkRenderer.display_text(metadata["alt"])
