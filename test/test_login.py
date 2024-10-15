from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5173")  # URL of your app

    def test_login_valid_credentials(self):
        # Wait for the login form to load
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Enter valid credentials
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "email").send_keys("client@gmail.com")  # Replace with valid username
        self.driver.find_element(By.NAME, "password").send_keys("123")  # Replace with valid password

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Verify that the user is redirected to the expense list or dashboard
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))  # Adjust based on your app

        # Add a delay to see the result
        time.sleep(3)  # Wait for 3 seconds before moving to the next test

    def test_login_invalid_credentials(self):
        # Wait for the login form to load
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Enter invalid credentials
        self.driver.find_element(By.NAME, "email").send_keys("wronguser@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")

        # Click the login button
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Verify that an error message is displayed
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error")))  # Adjust based on your app

        # Add a delay to see the result
        time.sleep(3)  # Wait for 3 seconds before the test ends

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
