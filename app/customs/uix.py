from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

from app.utils.calculate_window import CalculateWindow


class ImageWithBorder(Image):
    def __init__(self, show_border=False, **kwargs):
        super().__init__(**kwargs)
        if show_border:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                self.border = Line(
                    rectangle=(self.x, self.y, self.width, self.height), width=2
                )
            self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        """Update border position and size based on the image's position and size."""
        self.border.rectangle = (self.x, self.y, self.width, self.height)


class CustomButton(ButtonBehavior, ImageWithBorder):
    scale = NumericProperty(1.0)

    def __init__(
        self,
        app,
        destination="",
        click_sound_path="assets/sounds/sound_effect/click.mp3",
        show_border=True,
        clicked_scale_max=0.02,
        **kwargs,
    ):
        super(CustomButton, self).__init__(show_border=show_border, **kwargs)

        self.app = app

        self.destination = destination if destination != "" else None
        self.clicked_scale_max = clicked_scale_max

        self.click_sound = (
            SoundLoader.load(click_sound_path) if click_sound_path else None
        )

        self.scale_up: Animation | None = None
        self.scale_down: Animation | None = None

        self._calculate_size_hints()
        Window.bind(on_resize=lambda *args: self._calculate_size_hints())

        if self.click_sound:
            self.click_sound.bind(on_stop=self._trigger_screen_change)

    def _trigger_screen_change(self, *args):
        """Navigate to the target screen after the click animation completes."""
        if not self.destination:
            return

        if self.destination == "previous":
            self.app.back_screen()
        else:
            self.app.switch_screen(self.destination)

    def _calculate_size_hints(self):
        """Calculate the default and clicked size hints based on texture and window size."""

        default_scale = (self.size_hint_x, self.size_hint_y)

        click_scale_increase = (
            self.size_hint_x + self.clicked_scale_max,
            self.size_hint_y + self.clicked_scale_max,
        )

        self.scale_down = Animation(size_hint=default_scale, duration=0.2)
        self.scale_up = Animation(size_hint=click_scale_increase, duration=0.2)

    def on_touch_down(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return False

        if self.click_sound:
            self.click_sound.play()

        if self.scale_up:
            self.scale_up.start(self)

        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if self.scale_down:
                self.scale_down.start(self)

        return super().on_touch_up(touch)

    def jiggle_effect(self):
        """Create a 'jiggle' animation for the button."""
        jiggle = Animation(
            pos_hint={"x": self.pos_hint["x"] + 0.01, "y": self.pos_hint.get("y", 0.5)},
            duration=0.1,
        ) + Animation(
            pos_hint={"x": self.pos_hint["x"] - 0.01, "y": self.pos_hint.get("y", 0.5)},
            duration=0.1,
        )
        jiggle.start(self)

    def start_wiggle(self, repeat=True, duration=0.5):
        default_size_hint = (self.size_hint_x, self.size_hint_y)

        click_size_increase = (
            self.size_hint_x + self.clicked_scale_max,
            self.size_hint_y + self.clicked_scale_max,
        )

        anim = Animation(size_hint=click_size_increase, duration=duration) + Animation(
            size_hint=(
                self.size_hint_x - self.clicked_scale_max,
                self.size_hint_y - self.clicked_scale_max,
            ),
            duration=duration,
        )

        anim += Animation(size_hint=default_size_hint, duration=duration)
        anim.repeat = repeat
        anim.start(self)

    def stop_animation(self):
        Animation.cancel_all(self)

    def set_disabled_state(self, disable: bool, custom_color=None):
        """Disable the button and apply a grayscale effect if disabled, or a custom color if provided."""
        self.disabled = disable
        if disable:
            self.color = custom_color if custom_color else (0.5, 0.5, 0.5, 1)
        else:
            self.color = (1, 1, 1, 1)


class OutlinedLabel(Label):
    font_color = ListProperty([1, 0.85, 0, 1])
    outline_color = ListProperty([0, 0, 1, 1])
    outline_width = NumericProperty(3)
    custom_font_size = NumericProperty(50)

    def __init__(
        self,
        font_color=[1, 0.788, 0.157, 1],
        outline_color=[0, 0.5, 1, 1],
        outline_width=2,
        custom_font_size=50,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.font_color = font_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.custom_font_size = custom_font_size

        self.color = self.font_color
        self.font_size = f"{self.custom_font_size}sp"

        self.bind(
            outline_color=self.update_outline_color,
            outline_width=self.update_outline_width,
            custom_font_size=self.update_font_size,
            font_color=self.update_font_color,
        )

    def update_outline_color(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.outline_color)
            self.outline = Line(
                width=self.outline_width,
                rectangle=(self.x, self.y, self.width, self.height),
            )

    def update_outline_width(self, *args):
        self.outline.width = self.outline_width

    def update_font_size(self, *args):
        self.font_size = f"{self.custom_font_size}sp"

    def update_font_color(self, *args):
        self.color = self.font_color
