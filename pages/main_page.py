import random
import re
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):

    PAGE_URL = Links.HOST

    # *|Попап|*
    POPUP_ELEMENT = '//div[contains(@class,"NewsPopup_root")]'

    def popup_return_news_is_visible(self, visible=True):
        '''Функция проверяет что попап с новостями виден. \n
            True - подтверждает что попап виден \n
            False - подтверждает что попап не виден'''
        is_visible = False
        try:
            self.fast_wait.until(EC.visibility_of_element_located(
                ('xpath', self.POPUP_ELEMENT)))
            is_visible = True
        except TimeoutException:
            is_visible = False

        if visible:
            with allure.step(f'Проверка что попап "Новости" показан'):
                assert is_visible, 'Попап "Новости" не отображается'
        else:
            with allure.step(f'Проверка что попап "Новостей" скрыт'):
                assert not is_visible, 'Попап "Новости" отображается, но не должен'

    def popup_checking_header(self, text=''):
        '''Проверяет что есть заголовок и он не пуст. \n
            Если ввести текст, то проверит наличие указанного текста в заголовке'''
        element = self.visibility_element(
            f'{self.POPUP_ELEMENT}//div[contains(@class,"NewsPopup_header")]')
        assert element.text, 'Заголовок пуст'

        if text:
            assert text.lower() in element.text.lower(), f'В заголовке не найден текст "{
                text}". Текст элемента: "{element.text}"'

    def popup_checking_image(self, alt='', src=''):
        element = self.visibility_element(
            f'{self.POPUP_ELEMENT}//img[contains(@class,"NewsPopup_image")]')
        assert '/image/' in element.get_attribute('src')

        if alt:
            assert alt.lower() in element.get_attribute('alt').lower(
            ), f'В alt элемента не найден текст "{alt}". Текст alt: "{element.get_attribute('alt')}"'
        if src:
            assert src.lower() in element.get_attribute('src').lower(
            ), f'В ссылке элемента не найдено название "{src}". Ссылка: "{element.get_attribute('src')}"'

    def popup_checking_content(self, text=''):
        element = self.visibility_element(f'({self.POPUP_ELEMENT}//span)[2]')

        if text:
            assert text.lower() in element.text.lower(), f'В элементе не найден текст "{
                text}". Текст элемента: "{element.text}"'

    def popup_close(self):
        self.element_clickable(f'({self.POPUP_ELEMENT}//span)[1]').click()

    # *|Папа|*

    # *|Поиск стримеров|*

    def streamer_search_not_found(self):
        element = search_focus(self)

        element.send_keys('eijk123')

        self.visibility_element(
            '(//div[contains(@class, "CategoriesInput_notFound")])[1]')

        search_unfocus(self, element)

    def streamer_search_been_found(self):
        element = search_focus(self)

        element.send_keys('ejik')

        self.visibility_all_elements(
            '//div[contains(@class, "SearchInput_container")]//div[contains(@class, "ScrollableComponent_container")]/div')

        search_unfocus(self, element)

    # *|Поиск стримеров|*

    # *|Блок рекомендаций|*

    RECOMMEND_ROOT = '(//div[contains(@class, "Drawer_root_Id")])[1]'
    STREAMER_BLOCK = f'({RECOMMEND_ROOT}//div[contains(@class,"ChannelsList_container")]/div)'

    def recommend_is_open(self, is_open=True):
        '''Проверяет что рекомендации развернуты'''

        element = self.visibility_element(self.RECOMMEND_ROOT)

        if '240px' in element.get_attribute('style'):
            with allure.step(f'Проверка что блок рекомендаций развернут'):
                assert is_open, 'Блок рекомендаций открыт'
        elif '60px' in element.get_attribute('style'):
            with allure.step(f'Проверка что блок рекомендаций свернут'):
                assert not is_open, 'Блок рекомендаций закрыт'
        else:
            with allure.step('Проверка стиля блока рекомендаций'):
                assert AssertionError(
                    'Размер блока не соответствует размерам свернутого или развернутого элемента')

    def recommend_open_close_btn_click(self):
        self.element_clickable(f'{self.RECOMMEND_ROOT}/button').click()

    def recommend_not_null(self):
        self.visibility_all_elements(f'{self.RECOMMEND_ROOT}//div[contains(@class,"ChannelsList_container")]/div')

    def recommend_streamer_data_img(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.STREAMER_BLOCK)))

        element_img = self.visibility_element(f'{self.STREAMER_BLOCK}[{id}]//img')
        assert element_img.get_attribute('src') and 'avatar' in element_img.get_attribute(
            'src'), 'Ссылка в рекомендации пуста или не содержит пути для аватара'

    def recommend_streamer_data_text(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.STREAMER_BLOCK)))

        STREAMER_BLOCK_TEXT = f'({self.STREAMER_BLOCK}[{id}]//div[contains(@class, "ChannelsItem_text")]/div)[1]'
        STREAMER_BLOCK_TITLE = f'({self.STREAMER_BLOCK}[{id}]//div[contains(@class, "ChannelsItem_text")]/div)[2]'

        assert self.visibility_element(
            STREAMER_BLOCK_TEXT).text, 'Название стрима в рекомендации пусто'
        assert self.visibility_element(
            STREAMER_BLOCK_TITLE).text, 'Название категории в рекомендации пусто'

    def recommend_streamer_data_counter(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.STREAMER_BLOCK)))

        STREAMER_BLOCK_COUNTER = f'{self.STREAMER_BLOCK}[{id}]//div[contains(@class, "ViewersCounter")]/div'

        assert self.visibility_element(
            STREAMER_BLOCK_COUNTER), "Количество зрителей в рекомендации пусто"

    # *|Блок рекомендаций|*

    # *|Блок популярными категориями|*
    CATEGORIES_LIST = '(//div[contains(@class, "CatalogCategoriesList_list")])[1]/a'

    def categories_links_image(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.CATEGORIES_LIST)))
            
        element_a = self.visibility_element(f'{self.CATEGORIES_LIST}[{id}]')
        category_id = re.search(r"category/([\w-]+)", element_a.get_attribute('href'))
        element_background = self.visibility_element(f'{self.CATEGORIES_LIST}[{id}]/div[1]')
        el_bg = element_background.get_attribute('style')

        assert f'category/{category_id.group(1)}' in el_bg, f'\
            Id категории в url не совпадает с id в фоне. Id в url: "{category_id.group(1)}" | Id в фоне: "{el_bg}"'

    def categories_links_title(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.CATEGORIES_LIST)))
            
        element = self.visibility_element(f'{self.CATEGORIES_LIST}[{id}]/div[2]')

        assert element.text, 'У категории нет названия'

    def categories_links_counter(self, id=0):
        if not id:
            id = random.randint(1, len(self.visibility_all_elements(self.CATEGORIES_LIST)))

        element = self.visibility_element(f'{self.CATEGORIES_LIST}[{id}]/div[3]/div/div')

        assert element.text, 'У категории пустое поле для счетчика зрителей'
        
    # *|Блок популярными категориями|*


# *|Вспомогательные функции|*
def search_focus(_self):
    element = _self.element_clickable(
        '//input[contains(@class, "SearchInputView")]')
    element.click()
    element.clear()
    return element


def search_unfocus(_self, element):
    element.clear()
    _self.visibility_element('//div[contains(@class, "Top_root")]').click()
