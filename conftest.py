import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv(override=True)


def _app_url() -> str:
    return os.environ.get(
        "RCA_APP_URL",
        "https://celadon-duckanoo-625c0b.netlify.app/",
    )


@pytest.fixture(scope="session")
def app_url():
    return _app_url()


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")

    drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(0)
    drv.set_page_load_timeout(120)
    yield drv
    drv.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
