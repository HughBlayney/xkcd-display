from renderers.abstract_renderer import AbstractRenderer


class VirtualRenderer(AbstractRenderer):
    def display_image(self, image_path: str = "./resized.png", refresh_to_white: bool = True,
                      flip_vertical: bool = True):
        print("displaying image at path: " + image_path)

    def display_text(self, text: str, refresh_to_white: bool = True, flip_vertical: bool = True):
        print("displaying text at path: " + text)

