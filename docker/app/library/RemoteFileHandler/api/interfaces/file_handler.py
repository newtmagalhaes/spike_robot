from abc import ABC, abstractmethod

from .selenium_grid import FilePayload


class IFileHandler(ABC):
    @abstractmethod
    def __init__(self, download_path: str) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def DOWNLOAD_PATH(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def save_file_as_zip(self, payload: FilePayload):
        raise NotImplementedError()

    @abstractmethod
    def save_extracted_files(self, payload: FilePayload):
        raise NotImplementedError()
