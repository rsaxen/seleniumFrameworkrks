import pytest
import time
from utlities.Base import Base
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestLogin(Base):
    def test_login(self):
        try:
            logObj=self.get_logger()
            time.sleep(3)
            self.driver.maximize_window()
            logObj.info("Browser get opened")
            homePage = HomePage(self.driver)
            self.driver.implicitly_wait(20)
            homePage.cancel().click()
            homePage.searchBox().click()
            time.sleep(3)
            logObj.info('Search box got clicked')
            homePage.searchInput().send_keys("spider")
            time.sleep(3)
            homePage.movieOption().click()
            time.sleep(3)
            homePage.bookTicket().click()
            time.sleep(3)
            self.driver.switch_to.active_element
            homePage.threedimensionOption().click()
            time.sleep(3)
            self.take_screenshot(self.driver)
            assert True
        except:
            assert False
