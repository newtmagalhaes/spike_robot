from os import getenv

from requests import get, post
from robot.api import logger

from ..interfaces.selenium_grid import FilePayload, ISeleniumGrid


class API(ISeleniumGrid):
    def __init__(self) -> None:
        self._BASE_URL = getenv("GRID_URL", "http://localhost:4444")
        self._API_ENDPOINT = self._BASE_URL + "/session/{session_id}/se/files"
        logger.debug(f"Using '{self._BASE_URL}'")

    @property
    def API_ENDPOINT(self) -> str:
        return self._API_ENDPOINT

    def download_file_name(self, session_id: str, file_name: str) -> FilePayload:
        response = post(
            self.API_ENDPOINT.format(session_id=session_id),
            json={"name": file_name},
            timeout=(5, 5),
        )
        response.raise_for_status()
        resultado = response.json()
        value: FilePayload = resultado["value"]
        return value

    def get_file_names(self, session_id: str) -> list[str]:
        response = get(
            self._API_ENDPOINT.format(session_id=session_id),
            timeout=(5, 5),
        )
        response.raise_for_status()
        resultado: dict = response.json()
        names = self._extract_names_from_json(resultado)

        logger.info(f"'{len(names)}' Arquivos disponíveis para download", also_console=True)
        return names

    def _extract_names_from_json(self, json: dict) -> list[str]:
        assert isinstance(json, dict)

        value = json.get('value', {})
        assert isinstance(value, dict)

        names = value.get("names", [])
        assert isinstance(names, list)

        return names
