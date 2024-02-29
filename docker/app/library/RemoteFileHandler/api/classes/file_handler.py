from base64 import decodebytes
from io import BytesIO
from os.path import join
from zipfile import ZipFile

from robot.api import logger

from ..interfaces.selenium_grid import FilePayload
from ..interfaces.file_handler import IFileHandler


class FileHandler(IFileHandler):
    def save_file_as_zip(self, payload: FilePayload, dest: str):
        encoded_file = payload['contents']
        file_name = payload["filename"]
        name_without_extension = self.__remove_extension(file_name)
        decoded = decodebytes(encoded_file.encode("utf-8"))
        # gerar .zip
        file_path = join(dest, f"{name_without_extension}.zip")
        with open(file_path, "wb") as file:
            file.write(decoded)

    def __remove_extension(self, file_name: str) -> str:
        return file_name.rsplit(".", 1).pop(0)

    def save_extracted_files(self, payload: FilePayload, dest: str):
        content = payload["contents"]
        encoded = content.encode("utf-8")
        decoded = decodebytes(encoded)

        # criar arquivo descompactado
        with ZipFile(BytesIO(decoded)) as zf:
            logger.info(f"Arquivos: {zf.namelist()}", also_console=True)
            zf.extractall(dest)
