import pytest
from config.data import Data
from pages.main_page import MainPage
from pages.offline_streamer_page import OfflineStreamer


class BaseTest:

    data: Data

    main_page: MainPage
    offline_streamer: OfflineStreamer

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()

        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.offline_streamer = OfflineStreamer(driver)

    # def fast_authorization(self):
    #     self.login_page.open()
    #     self.login_page.enter_login(self.data.USER_LOGIN)
    #     self.login_page.enter_password(self.data.USER_PASSWORD)
    #     self.login_page.click_login_btn()
