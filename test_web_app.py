import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

APP_URL = os.environ.get("APP_URL", "http://localhost:8082")
EXPECTED_TITLE = os.environ.get("EXPECTED_TITLE", "")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

def test_page_has_title(driver):
    driver.get(APP_URL)
    assert driver.title.strip() != ""

def test_page_title_matches_expected(driver):
    driver.get(APP_URL)
    assert EXPECTED_TITLE in driver.title

def test_page_has_content(driver):
    driver.get(APP_URL)
    body = driver.find_element(By.TAG_NAME, "body")
    assert len(body.text.strip()) > 0
