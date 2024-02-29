from robot.api import logger
from robot.api.deco import keyword, library
from selenium.webdriver.common.options import BaseOptions

from .api.classes.api import API, FilePayload, ISeleniumGrid
from .api.classes.download_map import DownloadMap, IDownloadMap
from .api.classes.file_handler import FileHandler, IFileHandler
from .interface import IRemoteFileHandler
from .web_driver_config import set_downloadsEnabled_option


@library(scope='GLOBAL', version='0.1')
class RemoteFileHandler(IRemoteFileHandler):
    def __init__(self) -> None:
        self._file_map: IDownloadMap = DownloadMap()
        self._API: ISeleniumGrid = API()
        self._FILE_HANDLER: IFileHandler = FileHandler()

    @keyword
    def set_downloadsEnabled_option(self, options: BaseOptions) -> BaseOptions:
        """Adiciona às opções para o browser permitir download de arquivos"""

        options = set_downloadsEnabled_option(options)
        return options

    @keyword
    def list_download_files(self, session_id: str) -> "list[str]":
        assert isinstance(session_id, str)

        names = self._API.get_file_names(session_id)
        self._file_map.insert_unregistered_files(names)
        return names

    @keyword
    def list_undownloaded_files(self) -> list[str]:
        return self._file_map.list_undownloaded_files()

    @keyword
    def retrieve_download_files(self, session_id: str, filename: str):
        assert isinstance(session_id, str)
        assert isinstance(filename, str)

        value = self._API.download_file_name(session_id, filename)
        self._file_map.mark_file_as_downloaded(filename)
        return value

    @keyword
    def save_file_as_zip(self, value: FilePayload, dest: str):
        file_name = value["filename"]
        logger.info(f"Obteve arquivo(s) '{file_name}'", also_console=True)
        self._FILE_HANDLER.save_file_as_zip(value, dest)

    @keyword
    def save_extracted_file(self, value: FilePayload, dest: str):
        self._FILE_HANDLER.save_extracted_files(value, dest)
