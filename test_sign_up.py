import datetime
import allure
import pytest
from pages import sign_up_page

FIRST_NAME = "TEST"
LAST_NAME = "TEST"
USER_NAME = f"steshov{datetime.date.day}{datetime.date.month}{datetime.date.year}"
VALID_PASSWORD = "Qwerty123456!"
INVALID_LENGTH_PASSWORD = "qwe"
INVALID_CONFIRMATION_PASSWORD = "Qwerty12346"


@allure.suite("Sign up page")
@pytest.mark.smoke
class TestSignUpPage:

    def set_user_data(self, driver):
        sign_up_page.set_firstname(driver, FIRST_NAME)
        sign_up_page.set_lastname(driver, LAST_NAME)
        sign_up_page.set_username(driver, USER_NAME)

    @allure.description("Check that name error is visible")
    def test_name_error_visibility(self, driver):
        sign_up_page.open_google_signup_page(driver)
        sign_up_page.set_username(driver, USER_NAME)
        sign_up_page.set_password(driver, VALID_PASSWORD)
        sign_up_page.confirm_password(driver, VALID_PASSWORD)
        sign_up_page.next_button_click(driver)
        assert sign_up_page.name_error_visibility(driver)

    @allure.description("Check that password length error is visible")
    def test_name_error_visibility(self, driver):
        sign_up_page.open_google_signup_page(driver)
        self.set_user_data(driver)
        sign_up_page.set_password(driver, INVALID_LENGTH_PASSWORD)
        sign_up_page.confirm_password(driver, INVALID_LENGTH_PASSWORD)
        sign_up_page.next_button_click(driver)
        assert sign_up_page.password_length_error_visibility(driver)

    @allure.description("Check that password confirmation error is visible")
    def test_name_error_visibility(self, driver):
        sign_up_page.open_google_signup_page(driver)
        self.set_user_data(driver)
        sign_up_page.set_password(driver, VALID_PASSWORD)
        sign_up_page.confirm_password(driver, INVALID_CONFIRMATION_PASSWORD)
        sign_up_page.next_button_click(driver)
        assert sign_up_page.password_confirmation_error_visibility(driver)