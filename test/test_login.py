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
        cls.driver.get("http://localhost:5173") 

    def test_login_valid_credentials(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "email").send_keys("client@gmail.com")  
        self.driver.find_element(By.NAME, "password").send_keys("123")  

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))  

        time.sleep(3) 

    def test_login_invalid_credentials(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        self.driver.find_element(By.NAME, "email").send_keys("wronguser@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        time.sleep(3)  

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
