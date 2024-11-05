from kivy.clock import Clock
from kivy.core.audio import Sound, SoundLoader
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.screenmanager import FadeTransition, ScreenManager
from kivymd.app import MDApp

from app.db.json_store_config_manager import ConfigManager
from app.db.json_store_score_manager import ScoreManager
from app.screen.main_menu import MainMenu
from app.screen.select_level_menu import ChooseGameScreen
from app.screen_level_budaya import BudayaScreen
from app.screen_level_budaya.ceria import BudayaCeriaScreen
from app.screen_level_budaya.seru import BudayaSeruScreen
from app.screen_level_kemerdekaan import KebangsaanScreen
from app.screen_level_kemerdekaan.ceria import KebangsaanCeriaScreen
from app.screen_level_kemerdekaan.seru import KebangsaanSeruScreen
from app.utils.calculate_window import CalculateWindow

# NOTE: DEBUGGING
Logger.setLevel("DEBUG")

# NOTE: DEV SCREEN
# Window.size = CalculateWindow(Window.width, (9, 20)).get_size()
# Window.size = CalculateWindow(380, (9, 20)).get_size()
# Window.size = CalculateWindow(480, (9, 20)).get_size()

# NOTE: PROD SCREEN
Window.size = CalculateWindow(
    window_width=Window.width,
).get_size()

# NOTE: INIT FONTS
LabelBase.register(name="lazy_dog", fn_regular="assets/font/lazy_dog.ttf")
LabelBase.register(name="satoshi", fn_regular="assets/font/satoshi.ttf")
LabelBase.register(name="more_sugar", fn_regular="assets/font/more_sugar.ttf")
LabelBase.register(name="boorsok", fn_regular="assets/font/boorsok.ttf")


class NadaCilikApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Nada Cilik"

        self.configs_manager = ConfigManager()
        self.score_manager = ScoreManager()
        self.backsound = None

        self.screen_manager = ScreenManager(transition=FadeTransition(duration=0.5))
        self._init_screen()

        self.backsound: Sound = SoundLoader.load(
            "assets/sounds/sound_effect/backsound.mp3"
        )

        self._fade_interval = 0.1
        self._fade_out_step = 0.05
        self._fade_in_step = 0.05
        self._max_volume = 0.5

    def _init_screen(self):
        # NOTE: Home Menu
        self.screen_manager.add_widget(MainMenu(name="main_menu", app=self))
        self.screen_manager.add_widget(ChooseGameScreen(name="choose_game", app=self))

        # NOTE: Game Menu
        self.screen_manager.add_widget(BudayaScreen(name="lagu_budaya", app=self))
        self.screen_manager.add_widget(
            KebangsaanScreen(name="lagu_kebangsaan", app=self)
        )

        # NOTE: Game Play.
        self.screen_manager.add_widget(BudayaCeriaScreen(name="budaya_ceria", app=self))
        self.screen_manager.add_widget(BudayaSeruScreen(name="budaya_seru", app=self))

        self.screen_manager.add_widget(
            KebangsaanCeriaScreen(name="kebangsaan_ceria", app=self)
        )
        self.screen_manager.add_widget(
            KebangsaanSeruScreen(name="kebangsaan_seru", app=self)
        )

    def build(self):
        return self.screen_manager

    def on_start(self):
        if self.configs_manager.get("mute"):
            self.stop_backsound(immediate=True)
        else:
            self.play_backsound()

        return super().on_start()

    def on_stop(self):
        self.stop_backsound(immediate=True)
        return super().on_stop()

    def navigate_back(self):
        """Navigate to the previous screen."""
        self.screen_manager.current = self.screen_manager.previous()

    def switch_screen(self, screen_name):
        """Switch to a specified screen."""
        if not self.screen_manager:
            raise ValueError("Screen manager is not initialized.")
        self.screen_manager.current = screen_name

    def stop_backsound(self, immediate=False):
        """Stop the background sound, with optional fade-out effect."""
        if self.backsound:
            if immediate:
                self.backsound.stop()
            else:
                Clock.schedule_interval(self._fade_out_volume, self._fade_interval)

    def _fade_out_volume(self, dt):
        """Decrease volume gradually to fade out the background sound."""
        if self.backsound.volume > 0:
            self.backsound.volume = max(0, self.backsound.volume - self._fade_out_step)
        else:
            self.backsound.stop()
            return False

    def play_backsound(self):
        """Play the background sound with fade-in effect."""
        if self.backsound and self.backsound.state != "play":
            self.backsound.loop = True
            self.backsound.volume = 0
            self.backsound.play()
            Clock.schedule_interval(self._fade_in_volume, self._fade_interval)

    def _fade_in_volume(self, dt):
        """Increase volume gradually to fade in the background sound."""
        if self.backsound.volume < self._max_volume:
            self.backsound.volume = min(
                self._max_volume, self.backsound.volume + self._fade_in_step
            )
        else:
            return False


if __name__ == "__main__":
    NadaCilikApp().run()
