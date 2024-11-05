from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.uix.button import MDButton, MDFabButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from app.customs.image import CustomImage
from app.customs.uix import CustomButton, ImageWithBorder
from app.layouts.default_bg import WithDefaultBG
from app.utils.calculate_window import CalculateWindow


class MainMenu(WithDefaultBG):
    def __init__(self, app, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.app = app

        self.layout = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        self._init_mute()

        cloud_1 = Image(
            source="assets/img/main_menu/decorations/cloud_1.png",
            size_hint=(0.7, 0.7),
            pos_hint={"center_x": 0.99, "center_y": 0.9},
        )
        self.layout.add_widget(cloud_1)

        cloud_2 = Image(
            source="assets/img/main_menu/decorations/cloud_2.png",
            size_hint=(0.7, 0.7),
            pos_hint={"center_x": 0.1, "center_y": 0.8},
        )
        self.layout.add_widget(cloud_2)

        dec_1 = Image(
            source="assets/img/main_menu/decorations/dec_1.png",
            size_hint=(0.3, 0.3),
            pos_hint={"center_x": 0.8, "center_y": 0.6},
        )
        self.layout.add_widget(dec_1)

        dec_2 = Image(
            source="assets/img/main_menu/decorations/dec_2.png",
            size_hint=(0.3, 0.3),
            pos_hint={"center_x": 0.12, "center_y": 0.5},
        )
        self.layout.add_widget(dec_2)

        title = CustomImage(
            source="assets/img/main_menu/title.png",
            size=CalculateWindow(400, (16, 9)).get_size(),
            pos_hint={"center_x": 0.5, "center_y": 0.751},
        )
        title.wiggle_effect(duration=1)
        self.layout.add_widget(title)

        dec_3 = Image(
            source="assets/img/main_menu/decorations/dec_3.png",
            size=CalculateWindow(900, (16, 9)).get_size(),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
        )
        self.layout.add_widget(dec_3)

        play_button = CustomButton(
            app=self.app,
            destination="choose_game",
            source="assets/img/buttons/play.png",
            size_hint=(0.65, 0.12),
            pos_hint={"center_x": 0.5, "center_y": 0.26},
        )
        self.layout.add_widget(play_button)

        exit_button = CustomButton(
            app=self.app,
            source="assets/img/buttons/keluar.png",
            size_hint=(0.65, 0.12),
            pos_hint={"center_x": 0.5, "center_y": 0.09},
        )
        exit_button.bind(on_release=lambda *args: self.app.stop())
        self.layout.add_widget(exit_button)

        self.add_widget(self.layout)

    def _init_mute(self, *args):
        is_muted = self.app.configs_manager.get("mute") or False

        icon = (
            "assets/img/icons/mute.png" if is_muted else "assets/img/icons/unmute.png"
        )

        self.button_mute = CustomButton(
            app=self.app,
            source=icon,
            size_hint=(0.1, 0.05),
            pos_hint={"center_x": 0.1, "center_y": 0.95},
        )
        self.button_mute.bind(on_press=self._update_mute)
        self.add_widget(self.button_mute)

    def _update_mute(self, *args):
        is_muted = self.app.configs_manager.get("mute") or False

        if is_muted:
            self.button_mute.source = "assets/img/icons/unmute.png"
            self.app.backsound.play()
            self.app.configs_manager.set("mute", False)
        else:
            self.button_mute.source = "assets/img/icons/mute.png"
            self.app.backsound.stop()
            self.app.configs_manager.set("mute", True)
