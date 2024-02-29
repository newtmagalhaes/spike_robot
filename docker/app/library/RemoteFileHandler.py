from base64 import decodebytes
from io import BytesIO
from os import getenv, path
from zipfile import ZipFile

from requests import get, post
from robot.api import logger
from selenium.webdriver.common.options import BaseOptions


class RemoteFileHandler:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    _BASE_URL = getenv("REMOTE_URL", "http://localhost:4444")
    _API_ENDPOINT = _BASE_URL + "/session/{session_id}/se/files"
    _DOWNLOAD_DIR = path.join(path.abspath(path.dirname(__file__)), "../downloads")

    def set_downloadsEnabled_option(self, options: BaseOptions) -> BaseOptions:
        """Adiciona às opções que o browser deve permitir download de arquivos"""
        options.set_capability("se:downloadsEnabled", True)
        logger.debug("Este robô requer um nó que permita download")
        return options

    def list_download_files(self, session_id: str) -> "list[str]":
        assert isinstance(session_id, str)

        response = get(
            self._API_ENDPOINT.format(session_id=session_id),
            timeout=(5, 5),
        )
        response.raise_for_status()
        resultado = response.json()
        names = self._extract_names_from_json(resultado)

        logger.info(f"'{len(names)}' Arquivos disponíveis para download", also_console=True)
        return names

    def _extract_names_from_json(self, json: dict) -> "list[str]":
        assert isinstance(json, dict)

        value = json.get('value', {})
        assert isinstance(value, dict)

        names = value.get("names", [])
        assert isinstance(names, list)

        return names

    def retrieve_download_files(self, session_id: str, filename: str):
        assert isinstance(session_id, str)
        assert isinstance(filename, str)

        response = post(
            self._API_ENDPOINT.format(session_id=session_id),
            json={"name": filename},
            timeout=(5, None),
        )
        response.raise_for_status()
        resultado = response.json()
        value = resultado["value"]

        # "Base64EncodedStringContentsOfDownloadedFileAsZipGoesHere"
        encoded_file: str = value["contents"]
        file_name: str = value["filename"]
        name_without_extension = file_name.rsplit(".", 1).pop(0)
        logger.info(f"Obteve arquivo(s) '{file_name}'", also_console=True)

        decoded = decodebytes(encoded_file.encode("utf-8"))
        # gerar .zip
        with open(f"{self._DOWNLOAD_DIR}/dump/{name_without_extension}.zip", "wb") as file:
            file.write(decoded)

        # criar arquivo descompactado
        with ZipFile(BytesIO(decoded)) as zf:
            logger.info(f"Arquivos: {zf.namelist()}", also_console=True)
            zf.extractall(f"{self._DOWNLOAD_DIR}/")
