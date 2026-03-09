from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import get_logger
log = get_logger()

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self,locator_name,locator_value):
        element = None
        log.info(f"Getting element: {locator_name} with value: {locator_value}")
        if locator_name.endswith("_id"):
           element = self.wait.until(expected_conditions.visibility_of_element_located((By.ID, locator_value)))
        elif locator_name.endswith("_name"):
            element = self.wait.until(expected_conditions.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_name.endswith("_xpath"):
            element = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator_value)))
        elif locator_name.endswith("_css"):
            element = self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator_value)))
        elif locator_name.endswith("_class"):
            element =  self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_name.endswith("_linktext"):
            element = self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        return element


    def click_element(self,locator_name,locator_value):
        log.info(f"Clicking element: {locator_name} with value: {locator_value}")
        element = self.get_element(locator_name,locator_value)
        element.click()

    def type_text(self,locator_name,locator_value,text):
        log.info(f"Typing text: '{text}' into element: {locator_name} with value: {locator_value}")
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def retrieve_list_of_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def is_element_visible(self,locator_name,locator_value):
        try:
            element = self.get_element(locator_name, locator_value)
            return element.is_displayed()
        except:
            return False

    def is_element_enabled(self,locator_name,locator_value):
        try:
            element = self.get_element(locator_name, locator_value)
            return element.is_enabled()
        except:
            return False

