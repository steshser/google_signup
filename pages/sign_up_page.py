import allure
from pages.locators import SignUpPage
import pages.basepage as bp

GOOGLE_SIGNUP_PAGE = "https://accounts.google.com/signup"


def open_google_signup_page(driver):
    with allure.step("Open Google sign up page"):
        driver.get(GOOGLE_SIGNUP_PAGE)


def set_firstname(driver, firstname):
    with allure.step("Set firstname"):
        bp.input_text(driver, SignUpPage.FIRSTNAME_FIELD, firstname)


def set_lastname(driver, lastname):
    with allure.step("Set lastname"):
        bp.input_text(driver, SignUpPage.LASTNAME_FIELD, lastname)


def set_username(driver, username):
    with allure.step("Set username"):
        bp.input_text(driver, SignUpPage.USERNAME_FIELD, username)


def set_password(driver, password):
    with allure.step("Set password"):
        bp.input_text(driver, SignUpPage.PASSWORD_FIELD, password)


def confirm_password(driver, confirm_password):
    with allure.step("Confirm password"):
        bp.input_text(driver, SignUpPage.CONFIRM_PASSWORD_FIELD, confirm_password)


def next_button_click(driver):
    with allure.step("Click on the next button"):
        bp.find_element(driver, SignUpPage.NEXT_BUTTON).click()


def name_error_visibility(driver):
    with allure.step("Check visibility of name error"):
        return bp.is_element_visible(driver, SignUpPage.NAME_ERROR)


def password_length_error_visibility(driver):
    with allure.step("Check visibility of password length error"):
        return bp.is_element_visible(driver, SignUpPage.PASSWORD_LENGTH_ERROR)


def password_confirmation_error_visibility(driver):
    with allure.step("Check visibility of password confirmation error"):
        return bp.is_element_visible(driver, SignUpPage.PASSWORD_CONFIRMATION_ERROR)