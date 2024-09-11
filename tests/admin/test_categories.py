from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login import TestLogin
import time

class TestCategories(TestLogin):
    def test_click_on_categories(self, driver):
        catalog_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Catalog']"))
        )
        catalog_menu.click()
        categories_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/admin/categories') and contains(., 'Categories')]"))
        )
        categories_menu.click()

        page_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Categories']"))
        )
        assert page_heading.is_displayed(), "Categories page did not load correctly"
        