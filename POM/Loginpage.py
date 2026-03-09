from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage
from utils import logger

log = logger.get_logger()

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_name     = "username"
    password_name = "password"
    login_button_xpath = "//button[@type='submit']"
    Logo_check_xpath = "//div[@class='orangehrm-login-branding']"
    forgot_password_link_xpath = "//div[contains(@class,'login-forgot')]/p"
    username_locator_on_forgotpass_xpath = "//input[@name='username']"
    reset_password_button_xpath = "//div[@class='orangehrm-forgot-password-button-container']/button[@type='submit']"
    password_reset_confirmation_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
    password_reset_message_xpath = "(//p[@class='oxd-text oxd-text--p'])[1]"
    mainmenu_list_xpath = "//ul[ @class ='oxd-main-menu']//span"
    mainmenu_item_xpath = "//ul[@class='oxd-main-menu']//span[normalize-space()='{}']"
    add_user_button_xpath = "//i[contains(@class,'oxd-button-icon')]"
    add_user_form_xpath = "//h6[normalize-space()='Add User']"
    role_dropdown_xpath = "(//div[@class='oxd-select-text--after']/i)[1]"
    status_dropdown_xpath = "(//div[@class='oxd-select-text--after']/i)[2]"
    role_option_xpath = "//div[@role='option']//span[text()='{}']"
    employee_name_input_xpath = "//input[contains(@placeholder,'Type for hints')]"
    status_option_xpath ="//div[@class ='oxd-select-option' and @ role='option']/span[contains(text(),'{}')]"
    new_username_input_xpath = "(//div[@class='oxd-form-row user-password-row']/preceding::input[@class='oxd-input oxd-input--active'])[2]"
    new_password_input_xpath = "(//label[contains(text(),'Password')]/following::input[@class='oxd-input oxd-input--active'])[1]"
    confirm_new_password_input_xpath = "//label[contains(text(),'Confirm Password')]/following::input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//button[@type='submit']"
    created_username_xpath = "//div[@class='oxd-table-cell oxd-padding-cell' and contains(@style,'flex')]/div[contains(text(),'{}')]"
    User_search_button_xpath = "//button[@type='submit']"
    logout_button_xpath = "//a[@role='menuitem' and contains(text(),'Logout')]"
    user_profile_icon_xpath = "//i[contains(@class,'oxd-userdropdown-icon')]"
    employee_name_option_xpath = "//div[@role ='option']//span[contains(normalize-space(),'{}')]"
    search_input_xpath = "//label[contains(text(),'Username')]/following::input[@class='oxd-input oxd-input--active']"
    invalid_user_error_message_xpath = "//div[contains(@class,'oxd-alert-content')]/p"


    def enter_username(self, username):
        self.type_text("username_name", self.username_name, username)

    def enter_password(self, password):
        # fix: use the correct locator-name suffix for the password field
        self.type_text("password_name", self.password_name, password)

    def click_login_btn(self):
        self.click_element("login_btn_xpath", self.login_button_xpath)

    def logo_check(self):
        return self.is_element_visible("logo_check_xpath", self.Logo_check_xpath)

    def input_field_validation(self, field_name):
        if field_name == "username":
            return (self.is_element_visible("username_name", self.username_name)
                    and
                    self.is_element_enabled("username_name", self.username_name))
        elif field_name == "password":
            return (self.is_element_visible("password_name", self.password_name)
                    and
                    self.is_element_enabled("password_name", self.password_name))
        elif field_name == "login_button":
            return (self.is_element_visible("login_btn_xpath", self.login_button_xpath)
                    and
                  self.is_element_enabled("login_btn_xpath", self.login_button_xpath))
        else:
            log.error(f"Invalid field name: {field_name}")
            return False

    def is_error_message_displayed(self):
        error_message = self.retrieve_element_text("invalid_user_error_message_xpath",self.invalid_user_error_message_xpath)
        print(error_message)
        if error_message.__contains__("Invalid credentials"):
            return True
        else:
            return False


    def login_to_application(self, username, password):
        log.info("logging in with username: {} and password: {}".format(username, password))
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        # wait for the login result: either navigation to dashboard or an invalid-credentials error message
        try:
            self.wait.until(lambda d: "dashboard" in d.current_url or len(d.find_elements(By.XPATH, self.invalid_user_error_message_xpath)) > 0)
        except Exception as e:
            log.info(f"Timeout waiting for login result: {e}")

    def forgot_password_link_functionality(self):
        self.click_element("forgot_password_link_xpath", self.forgot_password_link_xpath)
        self.type_text("username_locator_on_forgotpass_xpath", self.username_locator_on_forgotpass_xpath, "vidhi")
        self.click_element("reset_password_button_xpath", self.reset_password_button_xpath)
        self.wait.until(EC.url_to_be(self.password_reset_confirmation_url))
        return self.retrieve_element_text("password_reset_message_xpath",self.password_reset_message_xpath)

    def get_main_menu_list(self):
        main_menu_elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.mainmenu_list_xpath)))
        main_menu_items = [element.text for element in main_menu_elements]
        return main_menu_items

    def validate_main_menu_list(self):

        main_menu_items = self.get_main_menu_list()

        for item in main_menu_items:
            log.info(f"Main menu item: {item}")
            final_mainmenu_item_xpath = self.mainmenu_item_xpath.format(item)
            if (self.is_element_visible("final_mainmenu_item_xpath", final_mainmenu_item_xpath)
                    and self.is_element_enabled("final_mainmenu_item_xpath", final_mainmenu_item_xpath)):
                log.info(f"Main menu item '{item}' is visible.")
            else:
                log.error(f"Main menu item '{item}' is not visible.")
                return False

        return True

    def navigate_to_user_management(self):
        log.info("Navigating to user management page")
        self.click_element("mainmenu_item_xpath", self.mainmenu_item_xpath.format("Admin"))
        self.wait.until(EC.url_contains("admin/viewSystemUsers"))

    def click_add_user_button(self):
        log.info("Clicking add user button")
        self.click_element("add_user_button_xpath", self.add_user_button_xpath)

    def add_user_role(self, role):
        log.info(f"Selecting user role: {role}")
        self.click_element("role_dropdown_xpath", self.role_dropdown_xpath)
        self.click_element("role_option_xpath", self.role_option_xpath.format(role))


    def add_status(self,  status):
        log.info(f"Selecting status: {status}")
        self.click_element("status_dropdown_xpath", "(//div[@class='oxd-select-text--after']/i)[2]")
        self.click_element("status_option_xpath", self.role_option_xpath.format(status))

    def enter_employee_name(self,  employee_name):
        log.info(f"Entering employee name: {employee_name}")
        self.type_text("employee_name_input_xpath", self.employee_name_input_xpath, employee_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.employee_name_option_xpath.format(employee_name))))
        self.click_element("employee_name_option_xpath", self.employee_name_option_xpath.format(employee_name))

    def enter_new_username(self,  new_username):
        log.info(f"Entering new username: {new_username}")
        self.type_text("new_username_input_xpath", self.new_username_input_xpath, new_username)

    def enter_new_password(self, new_password):
        log.info("Entering new password")
        self.type_text("new_password_input_xpath", self.new_password_input_xpath, new_password)

    def confirm_new_password(self,  new_password):
        log.info("Confirming new password")
        self.type_text("confirm_new_password_input_xpath", self.confirm_new_password_input_xpath, new_password)

    def click_save_button(self):
        log.info("Clicking save button")
        self.click_element("save_button_xpath", "//button[@type='submit']")
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.add_user_form_xpath)))

    def verify_user_creation(self, new_username):
        log.info(f"Verifying user creation for username: {new_username}")
        self.type_text("search_input_xpath", self.search_input_xpath, new_username)
        self.click_element("User_search_button_xpath", self.User_search_button_xpath)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.created_username_xpath.format(new_username))))
        return element.text == new_username

    def click_logout_button(self):
        log.info("Logging out of the application")
        self.click_element("user_profile_icon_xpath", self.user_profile_icon_xpath)
        self.click_element("logout_button_xpath", self.logout_button_xpath)
        self.wait.until(EC.url_contains("auth/login"))
