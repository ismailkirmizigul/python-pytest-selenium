import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenPositionsPage():
    filter_by_location_button = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    location_istanbul_option = (By.XPATH, "//ul/li[text()='Istanbul, Turkey']")
    job_list = (By.CSS_SELECTOR, "[id='jobs-list']")
    view_role = (By.XPATH, "//div[@id='jobs-list']//a[@href]")
    lever_form_url = (By.XPATH, "//head/meta[@property='og:url']")

    def __init__(self, browser):
        self.browser = browser

    def clickFilterByLocation(self):
        time.sleep(5)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.filter_by_location_button)).click()

    def selectLocationIstanbul(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.location_istanbul_option)).click()
        time.sleep(2)

    def jobsInList(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.job_list))

    def jobsSpecs(self, spec):
        jobList = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.job_list))

        if spec == "data-team":
            return jobList.find_elements(By.CSS_SELECTOR, "[data-team]")

        elif spec == "data-location":
            return jobList.find_elements(By.CSS_SELECTOR, "[data-location]")

        elif spec == "job-position":
            return jobList.find_elements(By.XPATH, ".//span")

        else:
            print("Wrong spec !!!")

    def clickViewRole(self):
        filter_button = self.browser.find_element(*self.filter_by_location_button)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", filter_button)
        time.sleep(1)

        view_roles = self.browser.find_elements(*self.view_role)
        view_roles[0].click()
        time.sleep(5)


