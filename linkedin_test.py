from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


# Define variables
base_url = "https://www.linkedin.com/"
user_email = "linkedintestautomation@gmail.com"
user_password = ""


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

    def test_notification(self):
        notification_field = self.driver.find_element(By.ID, 'notifications-tab-icon')
        notification_field.click()

        time.sleep(4)

    def test_profile(self):
        profile_field = self.driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/img')
        profile_field.click()
        time.sleep(5)
        view_profile = self.driver.find_element_by_css_selector('.nav-settings__linkcard-link')
        view_profile.click()
        time.sleep(5)

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
        mynetwork_field = self.driver.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]')
        mynetwork_field.click()
        time.sleep(5)

    def test_home(self):
        home_field = self.driver.find_element_by_xpath('//*[@id="feed-nav-item"]/a')
        home_field.click()
        time.sleep(7)

    def test_messages(self):
        message_field = self.driver.find_element_by_xpath('//*[@id="messaging-nav-item"]/a')
        message_field.click()
        time.sleep(4)

    def test_search_jobs(self):
        job_field = self.driver.find_element_by_xpath('//*[@id="jobs-tab-icon"]')
        job_field.click()
        time.sleep(4)
        search_field = self.driver.find_element_by_xpath('//input[contains(@id,"ember") and contains(@placeholder,"Search jobs")]')
        time.sleep(4)
        search_field.send_keys('Test Engineer')
        time.sleep(4)

    def test_sign_out(self):
        profile_field = self.driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/img')
        profile_field.click()
        time.sleep(3)
        sign_out_field = self.driver.find_element_by_link_text('Sign out')
        sign_out_field.click()
        time.sleep(5)

    def test_exit(self):
        print('Test Automation for Linkedin is finished')
        self.driver.quit()


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
