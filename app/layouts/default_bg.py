from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.screen import Screen


class WithDefaultBG(Screen):
    def __init__(self, **kwargs):
        super(WithDefaultBG, self).__init__(**kwargs)

        self.bg = Image(
            source="assets/img/bg.png",
            allow_stretch=True,
            keep_ratio=False,
        )
        self.add_widget(self.bg)
