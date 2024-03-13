import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    accept_cookies_button = (By.XPATH, "//*[@id='wt-cli-accept-all-btn']")
    company_button = (By.XPATH,"//div[@id='navbarNavDropdown']//li[6]/a[@id='navbarDropdownMenuLink']")
    careers_button = (By.XPATH, "//div[@id='navbarNavDropdown']//a[@href='https://useinsider.com/careers/']")

    def __init__(self, browser):
        self.browser = browser

    def clickAcceptAllCookies(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.accept_cookies_button)).click()

    def clickCompanyButton(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.company_button)).click()

    def clickCareersButton(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.careers_button)).click()

        WebDriverWait(self.browser, 30).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
