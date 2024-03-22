from base.base_test import BaseTest

class TestOfflineStreamer(BaseTest):

    def test_popup(self):
        self.offline_streamer.open()
        self.offline_streamer.is_opened()

        self.offline_streamer.player_is_visible()
        self.offline_streamer.followbutton_is_visible()
        self.offline_streamer.subscribebuttonbase_is_visible()
        self.offline_streamer.streamer_avatar_is_visible()
        self.offline_streamer.chat_is_visible()
