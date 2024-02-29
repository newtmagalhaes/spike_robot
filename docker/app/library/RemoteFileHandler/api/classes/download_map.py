from robot.api import logger

from ..interfaces.download_map import IDownloadMap

FileMap = dict[str,bool]


class DownloadMap(IDownloadMap):
    def __init__(self) -> None:
        self._file_map: FileMap = {}

    def list_undownloaded_files(self) -> list[str]:
        return [key for key, value in self._file_map.items() if value is False]

    def insert_unregistered_files(self, filenames: list[str]):
        for file in filenames:
            if file not in self._file_map:
                self._file_map[file] = False
                logger.debug(f"Inserting file '{file}'.")

    def mark_file_as_downloaded(self, filename: str):
        if filename not in self._file_map:
            logger.warn(f"File '{filename}' not in file_map but marked as downloaded.")

        self._file_map[filename] = True
        logger.debug(f"File '{filename}' marked as downloaded.")
