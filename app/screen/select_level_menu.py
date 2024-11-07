from kivymd.uix.floatlayout import MDFloatLayout

from app.customs.uix import CustomButton
from app.layouts.default_bg import WithDefaultBG


class ChooseGameScreen(WithDefaultBG):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app

        self.layout = MDFloatLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.setup_ui()

        self.add_widget(self.layout)

    def setup_ui(self):
        """Set up the UI components of the Choose Game Screen."""
        back_button = CustomButton(
            app=self.app,
            size_hint=(0.25, 0.1),
            destination="main_menu",
            source="assets/img/buttons/arrow_3.png",
            pos_hint={"center_x": 0.85, "center_y": 0.93},
        )
        self.layout.add_widget(back_button)

        self.budaya_button = CustomButton(
            app=self.app,
            source="assets/img/choice_menu_screen/budaya.png",
            size_hint=(0.7, 0.38),
            destination="lagu_budaya",
            pos_hint={"center_x": 0.5, "center_y": 0.67},
        )
        self.layout.add_widget(self.budaya_button)

        self.kebangsaan_button = CustomButton(
            app=self.app,
            destination="lagu_kebangsaan",
            source="assets/img/choice_menu_screen/kebangsaan.png",
            size_hint=(0.7, 0.38),
            pos_hint={"center_x": 0.5, "center_y": 0.26},
        )
        self.layout.add_widget(self.kebangsaan_button)

    def on_pre_enter(self, *args):
        """Start the wiggling animation for the buttons before entering the screen."""
        self.budaya_button.start_wiggle(duration=2)
        self.kebangsaan_button.start_wiggle(duration=2)
        return super().on_pre_enter(*args)

    def on_pre_leave(self, *args):
        """Stop the wiggling animation for the buttons before leaving the screen."""
        self.budaya_button.stop_animation()
        self.kebangsaan_button.stop_animation()
        return super().on_pre_leave(*args)
