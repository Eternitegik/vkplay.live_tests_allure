import allure
import pytest
from base.base_test import BaseTest


# @allure.feature("Проверка страницы авторизации")
# @pytest.mark.Authorization
class TestMain(BaseTest):

    # @allure.title("Проверка на успешную авторизацию")
    # @allure.severity("Critical")
    def test_popup(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.popup_return_news_is_visible()
        self.main_page.popup_checking_header()
        self.main_page.popup_checking_image()
        self.main_page.popup_checking_content()
        self.main_page.popup_close()
        self.main_page.popup_return_news_is_visible(False)

    def test_streamer_search(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.popup_close()

        self.main_page.streamer_search_not_found()
        self.main_page.streamer_search_been_found()

    def test_recommend(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.popup_close()

        self.main_page.recommend_is_open()
        self.main_page.recommend_not_null()
        self.main_page.recommend_streamer_data_img()
        self.main_page.recommend_streamer_data_text()
        self.main_page.recommend_streamer_data_counter()
        self.main_page.recommend_open_close_btn_click()
        self.main_page.recommend_is_open(False)

    def test_categories(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.popup_close()

        self.main_page.categories_links_image()
        self.main_page.categories_links_title()
        self.main_page.categories_links_counter()
