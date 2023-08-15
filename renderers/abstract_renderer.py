import abc


class AbstractDisplayDriver(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def display_image(image_path: str = "./resized.png"):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def display_text(text: str):
        raise NotImplementedError
