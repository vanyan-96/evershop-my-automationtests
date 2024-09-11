from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_categories import TestCategories

class TestAddCategory(TestCategories):
    def test_add_new_category(self, driver):
        self.test_click_on_categories(driver)
        new_category_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/admin/categories/new' and contains(@class, 'button primary')]"))
        )
        new_category_button.click()

        create_category_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Create A New category']"))
        )
        assert create_category_heading.is_displayed(), "Create New Category page did not load correctly"

        # Fill in the required fields to create a new category
        name_input = driver.find_element(By.ID, "name")
        urlKey_input = driver.find_element(By.ID, "urlKey")

        name_input.send_keys("Test Category")
        urlKey_input.send_keys("testCategory")

        # Submit the form
        save_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button primary') and contains(.,'Save')]")
        save_button.click()

        # Check if the category was created successfully
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body"))
        )
        assert success_message.text == "Category saved successfully!", "Category was not created successfully"
