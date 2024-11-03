from kivy.animation import Animation
from kivy.uix.image import Image


class CustomImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def wiggle_effect(self, duration: float = 0.8):
        initial_center_x = self.pos_hint.get("center_x", 0.5)
        # initial_center_y = self.pos_hint.get("center_y", 0.5)

        wiggle_animation = (
            Animation(pos_hint={"center_x": initial_center_x + 0.02}, duration=duration)
            + Animation(
                pos_hint={"center_x": initial_center_x - 0.02}, duration=duration
            )
            + Animation(
                pos_hint={"center_x": initial_center_x + 0.01}, duration=duration
            )
            + Animation(
                pos_hint={"center_x": initial_center_x - 0.01}, duration=duration
            )
            + Animation(pos_hint={"center_x": initial_center_x}, duration=duration)
        )

        wiggle_animation.repeat = True

        wiggle_animation.start(self)

    def clear_all_animations(self):
        Animation.cancel_all(self)

        self.angle = 0
