from abc import ABC, abstractmethod

from .selenium_grid import FilePayload


class IFileHandler(ABC):
    @abstractmethod
    def save_file_as_zip(self, payload: FilePayload, dest: str):
        raise NotImplementedError()

    @abstractmethod
    def save_extracted_files(self, payload: FilePayload, dest: str):
        raise NotImplementedError()
