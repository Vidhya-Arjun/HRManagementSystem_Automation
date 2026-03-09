
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()

class UserProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    My_info_xpath = "//span[contains(@class, 'oxd-main-menu-item--name') and normalize-space() = 'My Info']"
    Personal_details_xpath = "//a[@class='orangehrm-tabs-item --active' and normalize-space()='Personal Details']"
    emergency_contacts_xpath = "//a[@class='orangehrm-tabs-item' and normalize-space()='Emergency Contacts']"
    myinfo_mainmenu_list_xpath = "//div[@role='tab']/a[contains(@class,'orangehrm-tabs-item')]"
    myinfomenu_item_xpath = "//div[@role='tab']/a[contains(@class,'orangehrm-tabs-item') and normalize-space()='{}']"


    def click_myinfo_menu(self):
        self.click_element("My_info_xpath", self.My_info_xpath)
        self.wait.until(EC.url_contains("pim/viewPersonalDetails"))

    def get_myinfo_menulist(self):
        menu_elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.myinfo_mainmenu_list_xpath)))
        main_menu_items = [element.text for element in menu_elements]
        return main_menu_items

    def validate_myinfo_menu_list(self):

        main_menu_items = self.get_myinfo_menulist()

        for item in main_menu_items:
            log.info(f"Main menu item: {item}")
            final_myinfomenu_item_xpath = self.myinfomenu_item_xpath.format(item)
            if (self.is_element_visible("final_myinfomenu_item_xpath", final_myinfomenu_item_xpath)
                    and self.is_element_enabled("final_myinfomenu_item_xpath", final_myinfomenu_item_xpath)):
                log.info(f"Main menu item '{item}' is visible and clickable.")
            else:
                log.error(f"Main menu item '{item}' is not visible and clickable.")
                return False

        return True
