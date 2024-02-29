from robot.api import logger
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.options import BaseOptions

_DOWNLOAD_PREFERENCES = {
    # "safebrowsing.enabled": "false",
    "download.prompt_for_download": "false",
    # "browser.helperApps.neverAsk.saveToDisk": "application/csv",
    # "browser.helperApps.neverAsk.saveToDisk": "application/xml",
    # "browser.helperApps.neverAsk.saveToDisk": "application/pdf",
    # "browser.helperApps.neverAsk.saveToDisk": "application/xlsx",
    # "browser.helperApps.neverAsk.saveToDisk": "application/xls",
    # "browser.helperApps.neverAsk.saveToDisk": "application/txt",
}


def set_downloadsEnabled_option(options: BaseOptions) -> BaseOptions:
    """Adiciona às opções que o browser deve permitir download de arquivos"""
    assert isinstance(options, BaseOptions)

    options.set_capability("se:downloadsEnabled", True)

    if isinstance(options, FirefoxOptions):
        _set_firefox_options(options)
        logger.info("set FirefoxOptions", also_console=True)

    elif isinstance(options, ChromeOptions):
        _set_chrome_options(options)
        logger.info("set ChromeOptions", also_console=True)

    else:
        logger.warn(f"Unexpected option type '{options.__class__.__name__}' ")

    logger.debug("Este robô requer um nó que permita download")
    return options


def _set_firefox_options(options: FirefoxOptions):
    for name, value in _DOWNLOAD_PREFERENCES.items():
        options.set_preference(name, value)


def _set_chrome_options(options: ChromeOptions):
    options.add_experimental_option("prefs", _DOWNLOAD_PREFERENCES)
