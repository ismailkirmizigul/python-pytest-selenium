import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CareersPage():
    location_section = (By.XPATH, "//section[@id='career-our-location']")
    team_section = (By.XPATH, "//section[@id='career-find-our-calling']")
    life_section = (By.CSS_SELECTOR, "[data-id='a8e7b90']")
    see_all_teams_button = (By.XPATH, "//section[@id='career-find-our-calling']//a[text()='See all teams']")
    quality_assurance_button = (By.XPATH, "//section[@id='career-find-our-calling']//a[@href='https://useinsider.com/careers/quality-assurance/']")
    see_all_qa_jobs_button = (By.XPATH, "//section[@id='page-head']//a[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance']")

    def __init__(self, browser):
        self.browser = browser

    def locationSection(self):
        return self.browser.find_element(*self.location_section)

    def teamSection(self):
        return self.browser.find_element(*self.team_section)

    def lifeSection(self):
        return self.browser.find_element(*self.life_section)

    def focusTeamsSection(self):
        team_block = self.browser.find_element(*self.team_section)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", team_block)
        time.sleep(2)

    def clickSeeAllTeams(self):
        action = ActionChains(self.browser)
        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.see_all_teams_button))
        action.move_to_element(button).click().perform()

    def clickQualityAssurance(self):
        results = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.quality_assurance_button))

        self.browser.execute_script("arguments[0].scrollIntoView(true);", results[0])
        time.sleep(1)

        results[0].click()

    def clickSeeAllQaJobs(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.see_all_qa_jobs_button)).click()

        WebDriverWait(self.browser, 30).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
