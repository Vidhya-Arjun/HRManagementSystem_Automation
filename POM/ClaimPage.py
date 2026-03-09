import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()


class ClaimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Claim_menu_xpath = "//ul[@class='oxd-main-menu']//span[normalize-space()='Claim']"

    submit_claim_button_xpath = "//li[@class='oxd-topbar-body-nav-tab']/a[normalize-space()='Submit Claim']"

    event_select_xpath = "(//i[contains(@class, 'oxd-select-text--arrow')])[1]"

    select_event_xpath = "//div[@role='option']/span[normalize-space()='Accommodation']"

    Currency_select_xpath = "(//i[contains(@class, 'oxd-select-text--arrow')])[2]"

    currency_value_select_xpath = "//div[@role='option']/span[contains(text(),'India')]"

    remarks_input_xpath = "//div/textarea[contains(@class,'oxd-textarea')]"

    create_button_xpath = "//button[@type='submit']"

    Expenses_details_xpath = "(//button[@type='button' and normalize-space() = 'Add'])[1]"

    Expense_type_xpath = "//i[contains(@class,'oxd-select-text--arrow')]"

    Date_field_xpath = "//input[@placeholder='yyyy-dd-mm']"

    Amount_field_xpath = "//label[contains(@class,'oxd-input-field-required') and normalize-space()='Amount']/following::input[@class='oxd-input oxd-input--active']"

    Notes_field_nput_xpath = "//label[@class='oxd-label' and normalize-space() ='Note']/following::textarea"

    save_button_xpath = "//button[@type='submit']"

    to_ensure_record_creation_xpath = "//div[contains(@class,'orangehrm-horizontal-padding')]/span"

    EmployeeName_xpath = "(//label[normalize-space()='Employee Name']/following::input[@placeholder='Type for hints...'])[1]"

    Event_selection_xpath = "(//i[contains(@class,'oxd-select-text--arrow')])[1]"

    myclaim_tab_xpath ="//li[@class='oxd-topbar-body-nav-tab']/a[normalize-space()='My Claims']"

    Event_Name_xpath = "//div[@role='option']/span[normalize-space()='Accommodation']"

    from_date_xpath = "(//label[normalize-space()='From Date']/following::input[@placeholder='yyyy-dd-mm'])[1]"

    To_date_xpath = "//label[normalize-space()='To Date']/following::input[@placeholder='yyyy-dd-mm']"

    Reference_id_value_xpath = "//div[@class='oxd-autocomplete-option']/span"

    search_button_xpath = "//button[@type='submit']"

    Employee_claim_tab_click_xpath = "//a[@class='oxd-topbar-body-nav-tab-item' and normalize-space()='Employee Claims']"

    Reference_id_text_box_xpath = "(//input[contains(@placeholder,'Type for hints')])[2]"

    claim_id_reference_xpath = "(//div[@role='columnheader']/following::div[@role='cell' and contains(@class,'oxd-padding-cell')]/div)[1]"

    def initiate_claim(self):
        self.click_element("Claim_menu_xpath", self.Claim_menu_xpath)
        self.wait.until(EC.url_contains("claim/viewAssignClaim"))

    def click_submit_claim(self):
        self.click_element("submit_claim_button_xpath", self.submit_claim_button_xpath)
        self.wait.until(EC.url_contains("claim/submitClaim"))

    def create_claim_request(self):
        self.click_element("event_select_xpath", self.event_select_xpath)

        self.click_element("select_event_xpath", self.select_event_xpath)
        self.click_element("Currency_select_xpath", self.Currency_select_xpath)
        self.click_element("currency_value_select_xpath", self.currency_value_select_xpath)
        self.type_text("remarks_input_xpath", self.remarks_input_xpath, "Test claim data")
        self.click_element("create_button_xpath", self.create_button_xpath)

    def add_expense_details(self):
        self.wait.until(EC.url_contains("claim/submitClaim/id"))
        self.click_element("Expenses_details_xpath", self.Expenses_details_xpath)
        self.click_element("Expense_type_xpath", self.Expense_type_xpath)
        self.click_element("select_event_xpath", self.select_event_xpath)
        self.type_text("Date_field_xpath", self.Date_field_xpath, "2024-01-03")
        self.type_text("Amount_field_xpath", self.Amount_field_xpath, "1000")
        self.type_text("Notes_field_nput_xpath", self.Notes_field_nput_xpath, "Test expense details")
        self.click_element("save_button_xpath", self.save_button_xpath)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']/div[contains(text(),'Accommodation')]")))

    def retrieve_claim_id(self):
        self.click_element("myclaim_tab_xpath", self.myclaim_tab_xpath)
        claim_id = self.retrieve_element_text("claim_id_reference_xpath", self.claim_id_reference_xpath)
        log.info(f"Created claim ID: {claim_id}")
        return claim_id

    def validate_claim_presence_in_employee_tab(self):
        claim_id = self.retrieve_claim_id()
        self.click_element("Employee_claim_tab_click_xpath", self.Employee_claim_tab_click_xpath)
        self.type_text("Reference_id_text_box_xpath", self.Reference_id_text_box_xpath, claim_id)
        self.click_element("Reference_id_value_xpath", self.Reference_id_value_xpath)
        self.click_element("search_button_xpath", self.search_button_xpath)
        number_of_records_details =self.retrieve_element_text("to_ensure_record_creation_xpath", self.to_ensure_record_creation_xpath)
        log.info(f"Number of records found: {number_of_records_details}")
        return number_of_records_details.__contains__("(1) Record Found")







