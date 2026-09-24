"""Smart Test Selection sample - deliberately failing case (AFCQE-271).

Mirrors the mono-repo's sample-failure-test.py: the report needs at least
one selected test whose execution result is Failed.
"""

import os
import time

from selenium.webdriver.common.by import By

APP_URL = os.environ.get(
    "RCA_APP_URL",
    "https://celadon-duckanoo-625c0b.netlify.app/",
)


def test_sts_expected_failure(driver):
    driver.get(APP_URL)
    time.sleep(1)
    banner = driver.find_element(By.CSS_SELECTOR, "#welcome-banner").text
    assert banner == "This assertion is expected to fail"
