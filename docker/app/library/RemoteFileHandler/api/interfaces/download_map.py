from abc import ABC, abstractmethod


class IDownloadMap(ABC):
    @abstractmethod
    def insert_unregistered_files(self, filenames: list[str]):
        raise NotImplementedError()

    @abstractmethod
    def mark_file_as_downloaded(self, filename: str):
        raise NotImplementedError()

    @abstractmethod
    def list_undownloaded_files(self) -> list[str]:
        raise NotImplementedError()
