import abc


class AbstractDisplayDriver(abc.ABC):
    @abc.abstractmethod
    def display_image(self, image_path: str = "_data/resized.png"):
        raise NotImplementedError

    @abc.abstractmethod
    def display_text(self, text: str):
        raise NotImplementedError


class EPD480x800:
    width = 800
    height = 480

    @property
    def get_height(self):
        return self.height

    @property
    def get_width(self):
        return self.width
