import pytest

from POM.ClaimPage import ClaimPage
from POM.Loginpage import LoginPage
from POM.UserProfilePage import UserProfilePage
from POM.LeavePage import LeavePage
from utils.ExcelUtils import read_data

@pytest.mark.smoke
def test_home_url_accessibility(driver,config):

    """Created to check the url's existence and to check whether it is active"""

    login = LoginPage(driver)
    assert driver.current_url.__contains__("https://opensource-demo.orangehrmlive.com")
    assert login.logo_check() is True

@pytest.mark.parametrize("row, username, password, expected",read_data())
def test_login_with_multiple_credentials(driver,row,username,password,expected):

    """ Test case to validate user list from excel using excel reader utility"""

    login = LoginPage(driver)
    login.login_to_application(username,password)
    if expected.lower() == "valid":

       #workflow to check the user is valid and login is permitted

        if "dashboard" in driver.current_url:
            print(f"Row {row}: Valid login successful")
            login.click_logout_button()
        else:
            print(f"Row {row}: Valid login failed")
            pytest.fail(f"Row {row}: Valid login should succeed - current_url={driver.current_url!r}")

    # workflow to check the user is invalid and login is not permitted

    elif expected.lower() == "invalid":

        if login.is_error_message_displayed():
            print(f"Row {row}: Invalid login handled correctly")


        else:
            print(f"Row {row}: Invalid login not handled")

            pytest.fail(f"Row {row}: Invalid login should show error message - current_url={driver.current_url!r}")

def test_validate_presence_of_login_field(driver,config):
    # field validation
    login = LoginPage(driver)
    assert login.input_field_validation("username") is True
    assert login.input_field_validation("password") is True
    assert login.input_field_validation("login_button") is True

def test_validate_forgot_password_functionality(driver,config):
    # reset password check
    login = LoginPage(driver)
    assert login.forgot_password_link_functionality().__contains__("A reset password link has been sent to you via email")

def test_validate_main_menu_list(driver,config):

    # functionality to check whether menu list contains specified tab and user is able to navigate

    login = LoginPage(driver)
    login.login_to_application(config["username"], config["password"])
    assert driver.current_url.__contains__("dashboard")
    testdata = login.get_main_menu_list()
    print("testdata", testdata)
    assert login.validate_main_menu_list() is True


@pytest.mark.smoke
def test_create_new_user_and_verify_login(driver,config):

   #Create new user using admin credential and validate the user availability

    login = LoginPage(driver)
    login.login_to_application(config["username"], config["password"])
    assert driver.current_url.__contains__("dashboard")
    login.navigate_to_user_management()
    login.click_add_user_button()
    login.add_user_role('ESS')
    login.add_status('Enabled')
    login.enter_employee_name(config["employee_name"])
    login.enter_new_username(config["new_username"])
    login.enter_new_password(config["new_password"])
    login.confirm_new_password(config["new_password"])
    login.click_save_button()
    login.verify_user_creation(config["new_username"])
    login.click_logout_button()
    login.enter_username(config["new_username"])
    login.enter_password(config["new_password"])
    login.click_login_btn()
    assert driver.current_url.__contains__("dashboard")


def test_validate_new_user_creation(driver,config):

    # new user creation check

    login = LoginPage(driver)
    login.login_to_application(config["username"], config["password"])
    assert driver.current_url.__contains__("dashboard")
    login.navigate_to_user_management()
    assert login.verify_user_creation(config["new_username"]) is True


def test_validate_myinfo_accessibility(driver,config):

    #User to check the my info is available

    login = LoginPage(driver)
    userprofile = UserProfilePage(driver)
    login.login_to_application(config["username"], config["password"])
    userprofile.click_myinfo_menu()
    userprofile.get_myinfo_menulist()
    assert userprofile.validate_myinfo_menu_list() is True

def test_validate_leave_assignment_functionality(driver,config):

    #leave assignement and verification

    login = LoginPage(driver)
    leave = LeavePage(driver)
    login.login_to_application(config["username"], config["password"])
    leave.click_leave_menu()
    leave.click_assign_leave()
    leave.fill_assign_leave_form()
    assert leave.validate_leave_assignment_functionality() is True


def test_validate_claim_creation_functionality(driver,config):

    #verify claim is created and claim exist in dashboard

    login = LoginPage(driver)
    claim = ClaimPage(driver)
    login.login_to_application(config["username"], config["password"])
    claim.initiate_claim()
    claim.click_submit_claim()
    claim.create_claim_request()
    claim.add_expense_details()
    assert claim.validate_claim_presence_in_employee_tab() is True

