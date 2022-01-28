import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    # browser=request.config.getoption("browser_name")
    browser = 'chrome'
    if browser=='chrome':
        service = Service(executable_path="D:\\PYTHON\\driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    else:
        service = Service(executable_path="D:\\PYTHON\\driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    driver.get("https://in.bookmyshow.com/explore/home/delhi")
    request.cls.driver = driver
    yield
    driver.close()




