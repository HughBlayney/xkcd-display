import abc


class AbstractRenderer(abc.ABC):
    def display_image(self, image_path: str = "./resized.png", refresh_to_white: bool = True,
                      flip_vertical: bool = True):
        raise NotImplementedError

    def display_text(self, text: str, refresh_to_white: bool = True, flip_vertical: bool = True):
        raise NotImplementedError