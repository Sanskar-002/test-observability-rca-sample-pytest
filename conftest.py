"""Driver fixture for the Bad PR Causation pytest sample.

When invoked via `browserstack-sdk pytest tests/`, the SDK transparently
routes `webdriver.Remote(...)` calls to the BrowserStack hub using the
capabilities defined in `browserstack.yml`. We don't pass connection
details here — the SDK fills them in.
"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    drv = webdriver.Remote(options=chrome_options)
    yield drv
    drv.quit()
