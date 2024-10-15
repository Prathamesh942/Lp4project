from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5173")  # URL of your app

    def test_register_valid_credentials(self):
        # Wait for the registration form to load
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Navigate to registration page (if necessary)
        # self.driver.find_element(By.LINK_TEXT, "Register").click()  # Uncomment if there is a link to the registration page

        # Enter valid registration credentials
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "password").clear()
        
        self.driver.find_element(By.NAME, "name").send_keys("John Doe")  # Replace with valid name
        self.driver.find_element(By.NAME, "email").send_keys("client@gmail.com")  # Replace with valid email
        self.driver.find_element(By.NAME, "password").send_keys("123456")  # Replace with valid password

        # Click the register button
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Verify that the user is redirected or a success message is displayed
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))  # Adjust based on your app

        # Add a delay to see the result
        time.sleep(3)  # Wait for 3 seconds before moving to the next test

    def test_register_invalid_credentials(self):
        # Wait for the registration form to load
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        wait.until(EC.presence_of_element_located((By.NAME, "email")))
        

        # Enter invalid registration credentials
        self.driver.find_element(By.NAME, "name").send_keys("John Doe")
        self.driver.find_element(By.NAME, "email").send_keys("invalid_email")  # Invalid email format
        self.driver.find_element(By.NAME, "password").send_keys("123")  # Short password

        # Click the register button
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
