from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(browser):
    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = Options()
        options.add_argument("-private")
        return webdriver.Firefox()
    elif browser == "safari":
        return webdriver.Safari()
    elif browser == "opera":
        return webdriver.Opera()
    elif browser == "edge":
        return webdriver.Edge()
    elif browser == "ie":
        return webdriver.Ie()
    else:
        raise ValueError("Unsupported browser")