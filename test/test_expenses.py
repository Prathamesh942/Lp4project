from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class TestExpensesCRUD(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:5173")  
       
    @classmethod
    def test_01_login_valid_credentials(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "email").send_keys("client@gmail.com")  
        self.driver.find_element(By.NAME, "password").send_keys("123")  

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))  

        time.sleep(3)  

    def test_02_create_expense(self):
        self.driver.get("http://localhost:5173")  
        
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "amount")))

     
        self.driver.find_element(By.NAME, "amount").send_keys("100")
        self.driver.find_element(By.NAME, "title").send_keys("Test Expense")
        self.driver.find_element(By.NAME, "category").send_keys("Food") 

     
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        
        time.sleep(2)  
        self.assertIn("Test Expense", self.driver.page_source)

    def test_03_read_expense(self):
        time.sleep(2)  
        self.assertIn("Test Expense", self.driver.page_source)

    def test_04_update_expense(self):
        edit_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")  
        edit_button.click()

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "amount")))

        self.driver.find_element(By.NAME, "amount").clear() 
        self.driver.find_element(By.NAME, "amount").send_keys("150")
        self.driver.find_element(By.NAME, "title").clear()
        self.driver.find_element(By.NAME, "title").send_keys("Updated Test Expense")
        
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(2)  
        self.assertIn("Updated Test Expense", self.driver.page_source)

    def test_delete_expense(self):
        delete_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")  
        delete_button.click()

        time.sleep(1) 
       
        time.sleep(2)  
        self.assertNotIn("Updated Test Expense", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
