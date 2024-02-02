from selenium.webdriver import FirefoxOptions, FirefoxProfile
from selenium.webdriver.firefox.options import Options


class FirefoxConfig:
    def get_firefox_options(self, profile_path: str):
        options = FirefoxOptions()
        options.set_preference("browser.shell.checkDefaultBrowser", False)
        # options.set_preference("browser.helperApps.alwaysAsk.force", True)
        options.set_preference("firefox.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.manager.showAlertOnComplete", True)
        options.set_preference("browser.download.manager.useDownloadDir", True)
        options.enable_downloads = False

        # profile = FirefoxProfile()
        # options.profile = profile
        # profile = {"firefox_profile": profile_path}
        # profile = options.to_capabilities()
        # FirefoxProfile(profile_path)
        # profile["firefox_profile"] = profile_path
        # options.set_capability(**profile)
        return options