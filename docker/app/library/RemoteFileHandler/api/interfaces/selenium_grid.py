from abc import ABC, abstractmethod
from typing import Literal

FileNames = dict[Literal["names"],list[str]]
GetResponse = dict[Literal["value"],FileNames]

# "Base64EncodedStringContentsOfDownloadedFileAsZipGoesHere"
FilePayload = dict[Literal["filename","contents"], str]
PostResponse = dict[Literal["value"],FilePayload]


class ISeleniumGrid(ABC):
    @property
    @abstractmethod
    def API_ENDPOINT(self) -> str:
        raise NotImplementedError(f"'API_ENDPOINT' property not implemented")

    @abstractmethod
    def get_file_names(self, session_id:str) -> list[str]:
        raise NotImplementedError(f"Method '{self.get_file_names.__name__}' not implemented")

    @abstractmethod
    def download_file_name(self, session_id:str, file_name:str) -> FilePayload:
        raise NotImplementedError(f"Method '{self.download_file_name.__name__}' not implemented")
