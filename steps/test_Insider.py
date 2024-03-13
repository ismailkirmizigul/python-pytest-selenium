import time

from selenium.webdriver.common.by import By

from conftest import openWebPage
from pages.CareersPage import CareersPage
from pages.HomePage import HomePage
from pages.OpenPositions import OpenPositionsPage


def test_CheckInsiderHomePage(browser):
    openWebPage(browser)
    assert "#1 Leader in Individualized, Cross-Channel CX — Insider" in browser.title


def test_CheckInsiderCareersPage(browser):
    HomePage(browser).clickCompanyButton()
    HomePage(browser).clickCareersButton()

    assert CareersPage(browser).lifeSection().is_displayed()
    assert CareersPage(browser).teamSection().is_displayed()
    assert CareersPage(browser).locationSection().is_displayed()


def test_CheckQAJobList(browser):
    CareersPage(browser).focusTeamsSection()
    CareersPage(browser).clickSeeAllTeams()
    CareersPage(browser).clickQualityAssurance()
    CareersPage(browser).clickSeeAllQaJobs()

    assert OpenPositionsPage(browser).jobsInList().is_displayed()


def test_CheckQAJobDetails(browser):
    OpenPositionsPage(browser).clickFilterByLocation()
    OpenPositionsPage(browser).selectLocationIstanbul()

    for team in OpenPositionsPage(browser).jobsSpecs("data-team"):
        if team.get_attribute("data-team") == "qualityassurance":
            assert True
        else:
            print("There is a different job from Quality Assurance deparmant in filter!!!")
            assert False

    for location in OpenPositionsPage(browser).jobsSpecs("data-location"):
        if location.get_attribute("data-location") == "istanbul-turkey":
            assert True
        else:
            print("There is a different job from Istanbul/Turkey location in filter!!!")

    for position in OpenPositionsPage(browser).jobsSpecs("job-position"):
        if position.get_attribute("textContent") == "Quality Assurance":
            assert True
        else:
            print("There is a different position from Quality Assurance in filter!!!")
            assert False


def test_CheckRedirectionToApplicationForm(browser):
    OpenPositionsPage(browser).clickViewRole()

    handles = browser.window_handles
    for handle in handles:
        browser.switch_to.window(handle)
        if "https://jobs.lever.co/useinsider" in browser.current_url:
            print("Redirection is successful")
            print("Redirected URL:", browser.current_url)
            assert True
            break
