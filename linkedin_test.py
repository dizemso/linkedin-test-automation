from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import send_email
import logging
import os
from selenium.webdriver.support.select import Select


# Define variables
base_url = "https://www.linkedin.com/"
user_email = "linkedintestautomation@gmail.com"
user_password = ""


class LinkedinTestAutomation:

    def __init__(self):
        for file in os.scandir("log"):
            if file.name.endswith(".png"):
                os.unlink(file.path)
        self.driver = webdriver.Chrome()

    def test_init(self):
        logging.info('Test Automation for Linkedin is started')
        # window Maximize
        self.driver.maximize_window()
        # Open the Url
        self.driver.get(base_url)
        # Get title
        title = self.driver.title
        logging.info('Website name is: ' + str(title))
        # for waiting
        self.driver.implicitly_wait(10)

    def test_screenshot(self, testcase_name):
        destination_folder_name = "log/"
        file_name = str(testcase_name) + ".png"
        destination_file = destination_folder_name + file_name

        try:
            total_width = self.driver.execute_script("return document.body.offsetWidth")
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.set_window_size(total_width, total_height)
            screenshot = self.driver.save_screenshot(destination_file)
            logging.info("Screenshot saved to directory --> :: " + destination_file)
        except NotADirectoryError:
            logging.warning("Not a directory issue")

    def test_login(self):
        logging.info("Login test started")

        try:
            email_field = self.driver.find_element(By.ID, 'login-email')
            email_field.send_keys(user_email)

            password_field = self.driver.find_element(By.ID, 'login-password')
            password_field.send_keys(user_password)

            login_link = self.driver.find_element(By.ID, 'login-submit')
            login_link.click()
            time.sleep(4)
            logging.debug("The current Url: " + self.driver.current_url)
            if "feed" in self.driver.current_url:
                logging.info("Login test successful")
            else:
                raise Exception("Login test failed")
        except:
            logging.error("Login test failed")
            test_object.test_screenshot("test_login")
            test_object.test_exit()

    def test_notification(self):
        logging.info("Notification test started")

        try:
            notification_field = self.driver.find_element(By.ID, 'notifications-tab-icon')
            notification_field.click()
            time.sleep(2)
            if "notification" in self.driver.current_url:
                logging.info("Notification test successful")
            else:
                raise Exception("Notification test failed")

            time.sleep(4)
        except:
            logging.error("Notification test failed")
            test_object.test_screenshot("test_notification")

    def test_profile(self):
        logging.info("Profile test started")
        try:
            profile_field = self.driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/img')
            profile_field.click()
            time.sleep(2)
            view_profile = self.driver.find_element_by_css_selector('.artdeco-button--fluid')
            view_profile.click()
            time.sleep(2)
            print('url link ' + self.driver.current_url)
            if "linked-in-test-automation" in self.driver.current_url:
                logging.info("Profile test successful")
            else:
                raise Exception("Profile test failed")
            time.sleep(2)
        except:
            print('profile click error')
            logging.error("Profile test failed")
            test_object.test_screenshot("test_profile")

    # def test_add_skills(self):
    #     add_profile_field = self.driver.find_element_by_tag_name('data-control-name="profile_edit_fab"')
    #     add_profile_field.click()
    #     time.sleep(4)
    #
    #     skills_panel = self.driver.find_element_by_xpath('//*[@id="ember596"]')
    #     skills_panel.click()
    #
    #     time.sleep(5)
    def test_mynetwork(self):
        logging.info("My Network test started")
        try:
            mynetwork_field = self.driver.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]')
            mynetwork_field.click()
            time.sleep(2)
            if "mynetwork" in self.driver.current_url:
                logging.info("My Network test successful")
            else:
                raise Exception("My Network test failed")
            time.sleep(5)
        except:
            logging.error("My Network test failed")
            test_object.test_screenshot("test_mynetwork")

    def test_home(self):
        logging.info("Home test started")
        try:
            home_field = self.driver.find_element_by_xpath('//*[@id="feed-nav-item"]/a')
            home_field.click()
            time.sleep(2)
            if "feed" in self.driver.current_url:
                logging.info("Home test successful")
            else:
                raise Exception("Home test failed")
            time.sleep(7)
        except:
            logging.error("Home test failed")
            test_object.test_screenshot("test_home")

    def test_messages(self):
        logging.info("Messages test started")
        try:
            message_field = self.driver.find_element_by_xpath('//*[@id="messaging-nav-item"]/a')
            message_field.click()
            time.sleep(2)
            element_text = message_field.text
            logging.debug('Text on element is : ' + element_text)
            if "messaging" in self.driver.current_url:
                logging.info("Messages test successful")
            else:
                raise Exception("Messages test failed")
            time.sleep(4)
        except:
            logging.error("Messages test failed")
            test_object.test_screenshot("test_messages")

    def test_search_jobs(self):
        logging.info("Search Job test started")
        try:
            job_field = self.driver.find_element_by_xpath('//*[@id="jobs-tab-icon"]')
            job_field.click()
            time.sleep(4)
            search_field = self.driver.find_element_by_xpath('//input[contains(@id,"ember") and contains(@placeholder,"Search jobs")]')
            time.sleep(4)
            search_field.send_keys('Test Engineer')
            time.sleep(4)
            search_field.clear()
            if "job" in self.driver.current_url:
                logging.info("Search Job test successful")
            else:
                raise Exception("Search Job test failed")
            time.sleep(3)
        except:
            logging.error("Search Job test failed")
            test_object.test_screenshot("test_search_jobs")

    def test_sign_out(self):
        logging.info("Sign out test started")
        try:
            profile_field = self.driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/img')
            profile_field.click()
            time.sleep(3)
            sign_out_field = self.driver.find_element_by_link_text('Sign out')
            sign_out_field.click()
            time.sleep(2)
            if "https://www.linkedin.com/" == self.driver.current_url:
                logging.info("Sign out test successful")
            else:
                raise Exception("Sign out test failed")
            time.sleep(5)
        except:
            logging.error("Sign out test failed")
            test_object.test_screenshot("test_sign_out")

    def test_exit(self):
        logging.info("Exit test started")
        try:
            logging.info('Test Automation for Linkedin is finished')
            self.driver.quit()
        except:
            logging.error("Exit test failed")
            test_object.test_screenshot("test_exit")

        logging.info('Sending e-mail to recipients')
        log_dir = 'log'
        log_file = 'log/selenium_log.log'
        send_email.send_email(log_dir, log_file)
        sys.exit(1)


logging.basicConfig(filename='log/selenium_log.log', filemode='w', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
test_object = LinkedinTestAutomation()
test_object.test_init()
test_object.test_login()
test_object.test_notification()
test_object.test_profile()
test_object.test_mynetwork()
test_object.test_home()
test_object.test_messages()
test_object.test_search_jobs()
#test_object.test_add_skills()
test_object.test_sign_out()
test_object.test_exit()

