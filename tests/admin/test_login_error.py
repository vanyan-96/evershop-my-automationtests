import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginError:
    def test_wrong_password(self, driver):
        driver.get("http://localhost:3000/admin")

        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        email_input.send_keys("test@test.com")
        password_input.send_keys("wrongpassword")
        login_button.click()

        message =WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-critical"))
            )
        assert message.text == "Invalid email or password"