"""Bad PR Causation - RCA training signal (pytest parity for WDIO sample).

Six tests against a tiny static HTML page. Each branch represents a
different fault scenario:

- main / clean spec + clean app: all 6 pass
- bad-dev-pr: clean spec + broken HTML (URL points at the broken
  Netlify deployment); all 6 fail with app-side shapes
- bad-automation-pr: broken spec (wrong selectors / expected strings)
  + clean HTML (URL points at the clean Netlify deployment); all 6
  fail with spec-side shapes
"""

import os
import time

from selenium.webdriver.common.by import By


# On main / bad-dev-pr the spec is identical; only the URL changes between
# branches to reflect what production would look like if the PR were merged.
APP_URL = os.environ.get(
    "RCA_APP_URL",
    "https://celadon-duckanoo-625c0b.netlify.app/",
)


def _open(driver):
    driver.get(APP_URL)
    time.sleep(1)


def test_click_sign_in(driver):
    _open(driver)
    driver.find_element(By.CSS_SELECTOR, "#login-buton").click()


def test_welcome_banner(driver):
    _open(driver)
    banner = driver.find_element(By.CSS_SELECTOR, "#welcome-banner").text
    assert banner == "Welcome to Browserstack"


def test_profile_name(driver):
    _open(driver)
    profile = driver.find_element(By.CSS_SELECTOR, "#user-name").text
    assert profile == "John Doe"


def test_click_submit_order(driver):
    _open(driver)
    driver.find_element(By.CSS_SELECTOR, "#submitOrder").click()


def test_cart_count(driver):
    _open(driver)
    count = driver.find_element(By.CSS_SELECTOR, "#cart-count").text
    assert count == "three items"


def test_click_logout(driver):
    _open(driver)
    driver.find_element(By.CSS_SELECTOR, "#logout-btn").click()
