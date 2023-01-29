from selenium.webdriver.common.by import By


class SignUpPage:
    FIRSTNAME_FIELD = By.ID, "firstName"
    LASTNAME_FIELD = By.ID, "lastName"
    USERNAME_FIELD = By.ID, "username"
    PASSWORD_FIELD = By.NAME, "Passwd"
    CONFIRM_PASSWORD_FIELD = By.NAME, "ConfirmPasswd"
    SHOW_PASSWORD_CHECKBOX = By.XPATH, "//input[@type='checkbox']"
    NEXT_BUTTON = By.XPATH, "//div[@id='accountDetailsNext']//button"
    NAME_ERROR = By.ID, "nameError"
    PASSWORD_LENGTH_ERROR = By.XPATH, "//span[contains(text(), 'Пароль не может быть короче')]"
    PASSWORD_CONFIRMATION_ERROR = By.XPATH, "//span[contains(text(), 'Пароли не совпадают')]"