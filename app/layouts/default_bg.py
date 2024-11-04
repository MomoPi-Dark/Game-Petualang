from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen


class WithDefaultBG(MDScreen):
    def __init__(self, **kwargs):
        super(WithDefaultBG, self).__init__(**kwargs)

        self.bg_image = Image(
            source="assets/img/bg.png",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            fit_mode="fill",
        )
        self.add_widget(self.bg_image)
