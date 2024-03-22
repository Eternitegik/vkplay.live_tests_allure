import random
import re
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OfflineStreamer(BasePage):

    PAGE_URL = Links.OFFLINE_STREAMER

    def player_is_visible(self):
        self.visibility_element('//vk-video-player')

    def followbutton_is_visible(self):
        self.visibility_element('//button[contains(@class, "FollowButton_root")]')

    def subscribebuttonbase_is_visible(self):
        self.visibility_element('//button[contains(@class, "SubscribeButtonBase")]')

    def streamer_avatar_is_visible(self):
        element = self.visibility_element(' \
            //div[contains(@class, "StreamPanel_root")]//div[contains(@class, "Avatar_block")]/img')
        
        assert element.get_attribute('src') and 'avatar' in element.get_attribute('src')

    def chat_is_visible(self):
        self.visibility_element('//div[contains(@class, "Chat_root")]')