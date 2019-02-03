from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Define variables
base_url = "https://www.linkedin.com/"
user_email = "linkedintestautomation@gmail.com"
user_password =


class LinkedinTestAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_init(self):
        print('Test Automation for Linkedin is started')
        # window Maximize
        self.driver.maximize_window()
        # Open the Url
        self.driver.get(base_url)
        # Get title
        title = self.driver.title
        print('Website name is: ', str(title))
        # for waiting
        self.driver.implicitly_wait(10)

    def test_login(self):
        email_field = self.driver.find_element(By.ID, 'login-email')
        email_field.send_keys(user_email)

        password_field = self.driver.find_element(By.ID, 'login-password')
        password_field.send_keys(user_password)

        login_link = self.driver.find_element(By.ID, 'login-submit')
        login_link.click()

        time.sleep(7)

    def test_exit(self):
        print('Test Automation for Linkedin is finished')
        self.driver.quit()


test_object = LinkedinTestAutomation()
test_object.test_init()
test_object.test_login()
test_object.test_exit()
