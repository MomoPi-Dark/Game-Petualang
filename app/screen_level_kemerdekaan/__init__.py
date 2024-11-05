from kivymd.uix.floatlayout import MDFloatLayout

from app.customs.uix import CustomButton
from app.layouts.default_bg import WithDefaultBG


class KebangsaanScreen(WithDefaultBG):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app

        self.layout = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        self.setup_ui()

        self.add_widget(self.layout)

    def setup_ui(self):
        back_button = CustomButton(
            app=self.app,
            size_hint=(0.25, 0.1),
            destination="choose_game",
            source="assets/img/buttons/arrow_3.png",
            pos_hint={"center_x": 0.85, "center_y": 0.93},
        )
        self.layout.add_widget(back_button)

        ceria_button = CustomButton(
            app=self.app,
            size_hint=(0.9, 0.2),
            destination="kebangsaan_ceria",
            source="assets/img/select_level/kebangsaan/1.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
        )
        self.layout.add_widget(ceria_button)

        seru_button = CustomButton(
            app=self.app,
            size_hint=(0.9, 0.22),
            destination="kebangsaan_seru",
            source="assets/img/select_level/kebangsaan/2.png",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
        )
        self.layout.add_widget(seru_button)
