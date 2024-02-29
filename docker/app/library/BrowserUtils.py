from selenium.webdriver import FirefoxOptions
from robot.api import logger


class BrowserUtils:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def get_default_firefox_options(self) -> FirefoxOptions:
        options = FirefoxOptions()
        logger.info("Criando FirefoxOptions", also_console=True)
        return options
