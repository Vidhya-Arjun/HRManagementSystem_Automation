import datetime

import logger
import pytest
import yaml
from selenium import webdriver

from utils import driver_factory
from utils.logger import get_logger
from utils.driver_factory import get_driver
import os
from datetime import datetime
from pathlib import Path


log = get_logger()

@pytest.fixture(scope="session")
def config():
    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "configs" / "config.yaml"
    with open(config_path) as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="function")
def driver(config):
    log.info("Launching browser")
    driver = get_driver(config['browser'])
    driver.maximize_window()
    driver.get(config["base_url"])
    yield driver
    driver.quit()

# Create dynamic report file
def pytest_configure(config):
    report_dir = "Reports"
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    report_file = os.path.join(report_dir, f"Test_Report_{timestamp}.html")

    config.option.htmlpath = report_file
    config.option.self_contained_html = True


# Add extra info to report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver is not None:

            screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"

            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)