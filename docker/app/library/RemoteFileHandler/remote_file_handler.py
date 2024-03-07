from os.path import abspath, dirname, join

from robot.api import logger
from robot.api.deco import keyword, library
from selenium.webdriver.common.options import BaseOptions

from .api.classes.api import API, FilePayload, ISeleniumGrid
from .api.classes.file_handler import FileHandler, IFileHandler
from .interface import IRemoteFileHandler
from .web_driver_config import set_downloadsEnabled_option

_DEFAULT_DOWNLOAD_DIR = join(abspath(dirname(__file__)), "../../downloads")


@library(scope='GLOBAL', version='0.1')
class RemoteFileHandler(IRemoteFileHandler):
    def __init__(self) -> None:
        self._API: ISeleniumGrid = API()
        self._FILE_HANDLER: IFileHandler = FileHandler(_DEFAULT_DOWNLOAD_DIR)

    @keyword
    def set_downloadsEnabled_option(self, options: BaseOptions) -> BaseOptions:
        """Adiciona às opções que o browser deve permitir download de arquivos"""

        options = set_downloadsEnabled_option(options)
        return options

    @keyword
    def list_download_files(self, session_id: str) -> "list[str]":
        assert isinstance(session_id, str)

        names = self._API.get_file_names(session_id)
        return names

    @keyword
    def retrieve_download_files(self, session_id: str, filename: str):
        assert isinstance(session_id, str)
        assert isinstance(filename, str)

        value = self._API.download_file_name(session_id, filename)
        return value

    def save_file_as_zip(self, value: FilePayload):
        file_name = value["filename"]
        logger.info(f"Obteve arquivo(s) '{file_name}'", also_console=True)
        self._FILE_HANDLER.save_file_as_zip(value)

    def save_extracted_file(self, value: FilePayload):
        self._FILE_HANDLER.save_extracted_files(value)
