from abc import ABC, abstractmethod

from selenium.webdriver.common.options import BaseOptions


class IRemoteFileHandler(ABC):
    @abstractmethod
    def set_downloadsEnabled_option(self, options: BaseOptions) -> BaseOptions:
        raise NotImplementedError()

    @abstractmethod
    def list_download_files(self, session_id: str) -> "list[str]":
        raise NotImplementedError()

    @abstractmethod
    def retrieve_download_files(self, session_id: str, filename: str):
        raise NotImplementedError()
