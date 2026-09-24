"""Smart Test Selection sample - passing cases (AFCQE-271).

Added on sts-vrt-feature only. TCS sees these as new relative to
sts-vrt-base and force-includes them as "Changed", which is what the
Smart Test Selection report is asserted against.
"""

import os
import time

from selenium.webdriver.common.by import By

APP_URL = os.environ.get(
    "RCA_APP_URL",
    "https://celadon-duckanoo-625c0b.netlify.app/",
)


def _open(driver):
    driver.get(APP_URL)
    time.sleep(1)


def test_sts_welcome_banner(driver):
    _open(driver)
    banner = driver.find_element(By.CSS_SELECTOR, "#welcome-banner").text
    assert banner == "Welcome to Stackmate"


def test_sts_profile_name(driver):
    _open(driver)
    profile = driver.find_element(By.CSS_SELECTOR, "#profile-name").text
    assert profile == "John Doe"
