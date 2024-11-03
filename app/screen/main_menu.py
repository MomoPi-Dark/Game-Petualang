from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from app.customs.image import CustomImage
from app.layouts.default_bg import WithDefaultBG
from app.utils.calculate_window import CalculateWindow

# NOTE: DEV SCREEN
# Window.size = CalculateWindow(Window.width, (9, 20)).get_size()
# Window.size = CalculateWindow(380, (9, 16)).get_size()

# NOTE: PROD SCREEN
Window.size = Window.width, Window.height

# NOTE: INIT FONTS
LabelBase.register(name="lazy_dog", fn_regular="assets/font/lazy_dog.ttf")
LabelBase.register(name="satoshi", fn_regular="assets/font/satoshi.ttf")
LabelBase.register(name="more_sugar", fn_regular="assets/font/more_sugar.ttf")
LabelBase.register(name="boorsok", fn_regular="assets/font/boorsok.ttf")


class MainMenu(WithDefaultBG):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        layout = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        cloud_1 = Image(
            source="assets/img/main_menu/decorations/cloud_1.png",
            size_hint=(None, None),
            size=CalculateWindow(300, (20, 9)).get_size(),
            pos_hint={"center_x": 0.9, "center_y": 0.9},
        )
        layout.add_widget(cloud_1)

        cloud_2 = Image(
            source="assets/img/main_menu/decorations/cloud_2.png",
            size_hint=(None, None),
            size=CalculateWindow(300, (20, 9)).get_size(),
            pos_hint={"center_x": 0.1, "center_y": 0.8},
        )
        layout.add_widget(cloud_2)

        dec_1 = Image(
            source="assets/img/main_menu/decorations/dec_1.png",
            size_hint=(None, None),
            size=CalculateWindow(100, (20, 9)).get_size(),
            pos_hint={"center_x": 0.8, "center_y": 0.6},
        )
        layout.add_widget(dec_1)

        dec_2 = Image(
            source="assets/img/main_menu/decorations/dec_2.png",
            size_hint=(None, None),
            size=CalculateWindow(100, (20, 9)).get_size(),
            pos_hint={"center_x": 0.12, "center_y": 0.5},
        )
        layout.add_widget(dec_2)

        title = CustomImage(
            source="assets/img/main_menu/title.png",
            size_hint=(None, None),
            size=CalculateWindow(400, (20, 9)).get_size(),
            pos_hint={"center_x": 0.5, "center_y": 0.751},
        )
        title.wiggle_effect(duration=1)
        layout.add_widget(title)

        grass = Image(
            source="assets/img/main_menu/grass.png",
            size_hint=(None, None),
            size=CalculateWindow(500, (20, 9)).get_size(),
            pos_hint={"center_x": 0.5, "center_y": 0.150},
        )
        layout.add_widget(grass)

        mascot = Image(
            source="assets/img/main_menu/mascot.png",
            size_hint=(None, None),
            size=CalculateWindow(500, (20, 9)).get_size(),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        layout.add_widget(mascot)

        self.add_widget(layout)
