import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()


class LeavePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    leave_menu_xpath = "//ul[@class='oxd-main-menu']//span[normalize-space()='Leave']"
    leave_mainmenu_list_xpath = "//div[@role='tab']/a[contains(@class,'orangehrm-tabs-item')]"
    leavemenu_item_xpath = "//div[@role='tab']/a[contains(@class,'orangehrm-tabs-item') and normalize-space()='{}']"
    assign_leave_button_xpath = "//li[contains(@class,'oxd-topbar-body')]/a[contains(text(),'Assign Leave')]"
    employee_name_input_xpath = "//input[contains(@placeholder,'Type for hints')]"
    employee_name_select_xpath = "(//div[@role='option' and @class='oxd-autocomplete-option']/span)[1]"
    leave_type_input_xpath = "(//i[contains(@class,'select-text--arrow')])[1]"
    leave_type_select_xpath = "(//div[@role='option']//span[contains(text(),'CAN')])[1]"
    from_date_input_xpath = "(//label[contains(text(),'From Date')]/following::input[@placeholder='yyyy-dd-mm'])[1]"
    to_date_input_xpath = "(//label[contains(text(),'Date')]/following::input[@placeholder='yyyy-dd-mm'])[2]"
    duration_input_xpath = "(//i[contains(@class,'select-text--arrow')])[2]"
    duration_select_xpath = "//div[@role='option']//span[contains(text(),'Full Day')]"
    comments_input_xpath = "//textarea[contains(@class,'textarea')]"
    assign_button_xpath = "//button[@type='submit']"
    confirm_leave_xpath = "//button[normalize-space()='Ok']"
    my_leave_page_xpath = "//a[normalize-space()='My Leave']"
    my_leave_calendar_from_date_xpath = "(//div[@class='oxd-date-input']/i[contains(@class,'bi-calendar')])[1]"
    my_leave_calendar_to_date_xpath = "(//div[@class='oxd-date-input']/i[contains(@class,'bi-calendar')])[2]"
    my_leave_from_date_xpath = "//div[contains(@class,'oxd-calendar-date-wrapper')]/div[contains(@class,'today')]"
    my_leave_to_date_xpath = "//div[contains(@class,'oxd-calendar-date-wrapper')]/div[contains(@class,'today')]"
    search_button_xpath = "//button[@type='submit']"
    record_evaluation_xpath = "//div[contains(@class,'orangehrm-header-container')]/span"
    fromdate_calendar_xpath = "(//i[contains(@class,'bi-calendar')])[1]"
    select_from_date_xpath = "(//div[contains(@class,'oxd-calendar-date') and normalize-space()=3])[2]"
    Todate_calendar_xpath = "(//i[contains(@class,'bi-calendar')])[2]"
    select_to_date_xpath = "(//div[contains(@class,'oxd-calendar-date') and normalize-space()=3])[2]"


    def click_leave_menu(self):
        self.click_element("leave_menu_xpath", self.leave_menu_xpath)
        self.wait.until(EC.url_contains("eave/viewLeaveList"))

    def click_assign_leave(self):
        self.click_element("assign_leave_button_xpath", self.assign_leave_button_xpath)
        self.wait.until(EC.url_contains("leave/assignLeave"))

    def fill_assign_leave_form(self):
        self.type_text("employee_name_input_xpath", self.employee_name_input_xpath, "manda")
        self.click_element("employee_name_select_xpath", self.employee_name_select_xpath)
        self.click_element("leave_type_input_xpath", self.leave_type_input_xpath)
        self.click_element("leave_type_select_xpath", self.leave_type_select_xpath)
        self.click_element("fromdate_calendar_xpath", self.fromdate_calendar_xpath)
        self.click_element("select_from_date_xpath", self.select_from_date_xpath)
        self.click_element("Todate_calendar_xpath", self.Todate_calendar_xpath)
        self.click_element("select_to_date_xpath", self.select_to_date_xpath)
        self.click_element("assign_button_xpath", self.assign_button_xpath)
        self.click_element("confirm_leave_xpath", self.confirm_leave_xpath)

    def validate_leave_assignment_functionality(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.assign_button_xpath)))
        self.click_element("my_leave_page_xpath", self.my_leave_page_xpath)
        self.click_element(
            "my_leave_calendar_from_date_xpath", self.my_leave_calendar_from_date_xpath)
        self.click_element("my_leave_from_date_xpath",self.my_leave_from_date_xpath)
        self.click_element(
            "my_leave_calendar_to_date_xpath", self.my_leave_calendar_to_date_xpath)
        self.click_element("my_leave_to_date_xpath",self.my_leave_to_date_xpath)
        time.sleep(3)

        self.click_element("search_button_xpath", self.search_button_xpath)
        record_text = self.retrieve_element_text("record_evaluation_xpath", self.record_evaluation_xpath)
        print(record_text)
        return "Records Found" in record_text and "(0)" not in record_text


