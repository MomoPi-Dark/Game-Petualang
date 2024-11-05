from kivy.clock import Clock
from kivy.core.audio import Sound, SoundLoader
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from app.customs.image import CustomImage
from app.customs.uix import CustomButton, OutlinedLabel
from app.layouts.default_bg import WithDefaultBG


class LayoutQuest(FloatLayout):
    __events__ = ("on_complete", "on_timeout", "on_go_home")

    def __init__(
        self,
        app,
        background_image: str,
        home_screen: str,
        timeout_bar_image: str,
        question: str,
        correct_answer: str,
        option_a_image: str,
        option_b_image: str,
        option_c_image: str,
        background_music: str = "",
        content_font_size: str = 20,
        timeout_duration: float = 10.0,
        decorations: list[CustomImage] = [],
        **kwargs,
    ):
        super(LayoutQuest, self).__init__(**kwargs)

        self.app = app
        self.home_screen = home_screen
        self.background_image = background_image
        self.question = question
        self.timeout_bar_image = timeout_bar_image
        self.content_font_size = content_font_size
        self.decorations = decorations
        self.option_images = [option_a_image, option_b_image, option_c_image]

        self.timeout_duration = timeout_duration
        self.elapsed_time = 0
        self.remaining_time = int(timeout_duration)
        self.correct_answer = correct_answer
        self.answered = False
        self.user_answer = ""

        self.wrong_sound: Sound | None = SoundLoader.load(
            "assets/sounds/sound_effect/fail.mp3"
        )
        self.correct_sound: Sound | None = SoundLoader.load(
            "assets/sounds/sound_effect/correct.mp3"
        )
        self.bg_music: Sound | None = (
            SoundLoader.load(background_music) if background_music else None
        )

        self.timeout_event = None
        self._check_called = False

        Clock.schedule_once(self._verify_call)

    def _verify_call(self, dt):
        if not self._check_called:
            raise ValueError("Quest not initiated with call_screen().")

    def _initialize_ui(self):
        """Set up the UI components for the quest layout."""
        background = Image(
            source=self.background_image,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            fit_mode="fill",
        )
        self.add_widget(background)

        home_button = CustomButton(
            app=self.app,
            source="assets/img/buttons/home.png",
            size_hint=(0.35, 0.07),
            destination=self.home_screen,
            pos_hint={"x": 0.02, "top": 0.99},
        )
        home_button.bind(on_press=self.reset_quest)
        self.add_widget(home_button)

        timeout_bar = CustomImage(
            source=self.timeout_bar_image,
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.73, "center_y": 0.95},
        )
        self.add_widget(timeout_bar)

        self.timeout_label = Label(
            text=f"{int(self.timeout_duration)} Detik",
            font_name="boorsok",
            font_size="30sp",
            pos_hint={"center_x": 0.78, "center_y": 0.95},
        )
        self.add_widget(self.timeout_label)

        self._create_lyrics_layout()

        self._initialize_option_buttons()

    def _create_lyrics_layout(self):
        """Create and configure the lyrics layout."""
        quest = CustomImage(
            source=self.question,
            pos_hint={"center_x": 0.5, "center_y": 0.65},
        )
        self.add_widget(quest)

        for deco in self.decorations:
            if deco.parent:
                deco.parent.remove_widget(deco)
            self.add_widget(deco)

    def _initialize_option_buttons(self):
        """Initialize answer buttons and set their positions."""
        y_position = 0.35
        self.answer_buttons = []

        for i, option_image in enumerate(self.option_images):
            button = CustomButton(
                app=self.app,
                source=option_image,
                size_hint=(0.9, 0.08),
                pos_hint={"center_x": 0.5, "center_y": y_position},
                click_sound_path="",
            )
            button.bind(
                on_press=lambda instance, *args, index=i: self._evaluate_answer(
                    chr(97 + index)
                )
            )
            self.add_widget(button)
            self.answer_buttons.append(button)
            y_position -= 0.1

    def reset_quest(self, *args):
        """Reset the quest and go to the home screen."""
        self.stop_quest()

        if not self.app.configs_manager.get("mute"):
            self.app.play_backsound()

    def _evaluate_answer(self, answer):
        """Evaluate the user's answer and update the UI accordingly."""
        if self.answered:
            return

        self.answered = True
        self.user_answer = answer
        is_correct = answer == self.correct_answer.lower()

        if self.timeout_event:
            self.timeout_event.cancel()

        (self.correct_sound if is_correct else self.wrong_sound).play()
        self.disable_buttons(True)

        self.dispatch("on_complete", is_correct, answer, self.remaining_time)

        if self.bg_music:
            self.bg_music.stop()

    def disable_buttons(self, disable: bool):
        """Disable answer buttons and indicate correctness using colors."""
        colors = [
            (0, 1, 0, 1) if chr(97 + i) == self.correct_answer.lower() else (1, 0, 0, 1)
            for i in range(3)
        ]
        for button, color in zip(self.answer_buttons, colors):
            button.set_disabled_state(disable, custom_color=color)

    def _update_timer(self, dt):
        """Update the countdown timer and trigger timeout if necessary."""
        self.elapsed_time += dt
        self.remaining_time = max(0, int(self.timeout_duration - self.elapsed_time))

        self.timeout_label.text = f"{self.remaining_time} Detik"

        if self.remaining_time == 0:
            self.handle_timeout()

    def handle_timeout(self):
        """Handle the event when the timer reaches zero."""
        if not self.answered:
            self.answered = True

            self.wrong_sound.play()
            self.disable_buttons(True)

            self.timeout_event.cancel()
            self.dispatch("on_timeout", 0)
            self.dispatch("on_complete", False, None, 0)

    def call_screen(self):
        """Initialize and start the quest screen."""
        self._check_called = True

        self._initialize_ui()

        self.dispatch("on_timeout", int(self.timeout_duration))
        self.timeout_event = Clock.schedule_interval(self._update_timer, 1)

        if self.bg_music:
            self.bg_music.volume = 0.5
            self.bg_music.play()

    def stop_quest(self):
        """Stop the quest and reset relevant properties."""
        if self.timeout_event:
            self.timeout_event.cancel()
            self.timeout_event = None

        if self.bg_music:
            self.bg_music.stop()

        self.answered = False
        self.elapsed_time = 0
        self.remaining_time = int(self.timeout_duration)
        self.timeout_label.text = f"{self.remaining_time} Detik"

        self.disable_buttons(False)

    def on_complete(self, is_correct, answer, remaining_time):
        pass

    def on_timeout(self, remaining_time):
        pass

    def on_go_home(self):
        pass


class LayoutFinish(FloatLayout):
    __events__ = ("on_go_home", "on_restart_quest")

    def __init__(self, app, group_key_store, key_store, destination, **kwargs):
        super(LayoutFinish, self).__init__(**kwargs)

        self.app = app

        store: dict = app.score_manager.get_score(group_key_store, key_store)

        last_score: dict = store.get("last_score", None)
        score_last_score = last_score.get("score", 0)

        best_score: dict = store.get("best_score", None)
        score_best_score = best_score.get("score", 0)

        background = Image(
            source="assets/img/bg.png",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            fit_mode="fill",
        )
        self.add_widget(background)

        celeb = CustomImage(
            source="assets/img/quest/finish/celebration.png",
            size_hint=(0.98, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            fit_mode="fill",
        )
        celeb.zoom_in_out_effect(duration=2)
        self.add_widget(celeb)

        self.finish_box = CustomImage(
            source="assets/img/quest/finish/finish_box.png",
            size_hint=(0.8, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
        )
        self.add_widget(self.finish_box)

        font_size = 41

        self.label_score = OutlinedLabel(
            text="Score",
            custom_font_size=font_size,
            font_name="boorsok",
            pos_hint={"center_x": 0.5, "center_y": 0.82},
        )
        self.add_widget(self.label_score)
        self.label_result_score = OutlinedLabel(
            text=f"{score_last_score}",
            custom_font_size=font_size,
            font_name="boorsok",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
        )
        self.add_widget(self.label_result_score)

        self.label_best_score = OutlinedLabel(
            text="Best Score",
            custom_font_size=font_size,
            font_name="boorsok",
            pos_hint={"center_x": 0.5, "center_y": 0.66},
        )
        self.add_widget(self.label_best_score)
        self.label_result_best_score = OutlinedLabel(
            text=f"{score_best_score}",
            custom_font_size=font_size,
            font_name="boorsok",
            pos_hint={"center_x": 0.5, "center_y": 0.59},
        )
        self.add_widget(self.label_result_best_score)

        d1 = CustomImage(
            size_hint=(0.7, 1),
            source="assets/img/quest/finish/d1.png",
            pos_hint={"center_x": 0.8, "center_y": 0.05},
        )
        self.add_widget(d1)

        d2 = CustomImage(
            size_hint=(0.7, 1),
            source="assets/img/quest/finish/d2.png",
            pos_hint={"center_x": 0.25, "center_y": 0.3},
        )
        self.add_widget(d2)
        button_restart = CustomButton(
            app=app,
            size_hint=(0.65, 0.12),
            source="assets/img/quest/finish/mulai_ulang.png",
            pos_hint={"center_x": 0.5, "center_y": 0.26},
        )
        button_restart.bind(
            on_press=lambda instance, *args: self.dispatch("on_restart_quest")
        )
        self.add_widget(button_restart)

        button_main_menu = CustomButton(
            app=app,
            size_hint=(0.65, 0.12),
            source="assets/img/quest/finish/main_menu.png",
            destination=destination,
            pos_hint={"center_x": 0.5, "center_y": 0.09},
        )
        button_main_menu.bind(
            on_press=lambda instance, *args: self.dispatch("on_go_home")
        )
        self.add_widget(button_main_menu)

        self.bg_sound = SoundLoader.load("assets/sounds/sound_effect/finish.mp3")

        if self.bg_sound:
            self.bg_sound.volume = 1
            self.bg_sound.play()

    def on_go_home(self):
        pass

    def on_restart_quest(self):
        pass


class LayoutScreen(WithDefaultBG):
    def __init__(
        self,
        app,
        group_key_store: str,
        key_store: str,
        questions_data: list[dict],
        home_destination: str,
        bar_timeout_src: str,
        timeout_duration=10.0,
        **kw,
    ):
        super(LayoutScreen, self).__init__(**kw)

        self.app = app
        self._questions_data = questions_data
        self._home_destination = home_destination
        self._bar_timeout_src = bar_timeout_src
        self._timeout_duration = timeout_duration
        self._group_key_store = group_key_store
        self._key_store = key_store

        self.bg_image_path = "assets/img/bg.png"

        self.base_layout = FloatLayout()
        self.add_widget(self.base_layout)

        self.current_question_index = 0
        self.current_question = None
        self.questions_cache = []
        self.start_time = None
        self._next_schedule = None
        self.finish = None

    def _reset_screen_layout(self):
        """Clear the layout for the next question or screen reset."""
        self.base_layout.clear_widgets()

    def _reset_cache(self):
        """Reset quiz-related data for a fresh start."""
        self.current_question_index = 0
        self.current_question = None
        self.questions_cache = []
        self.start_time = None

    def is_quiz_complete(self):
        """Check if all questions have been answered."""
        return self.current_question_index >= len(self._questions_data)

    def _show_question(self):
        """Display the current question on the screen."""

        if self.start_time == None:
            self.start_time = Clock.get_time()

        if self.current_question:
            self.base_layout.remove_widget(self.current_question)
            self.current_question = None

        if self.is_quiz_complete():
            self._finish_quiz()
            return

        question_data = self._questions_data[self.current_question_index]

        self.current_question = LayoutQuest(
            app=self.app,
            background_image=self.bg_image_path,
            home_screen=self._home_destination,
            timeout_bar_image=self._bar_timeout_src,
            background_music=question_data.get("bg_sound", ""),
            content_font_size=question_data.get("font_content_size", "20sp"),
            timeout_duration=self._timeout_duration,
            question=question_data.get("question", None),
            correct_answer=question_data.get("answer", ""),
            decorations=question_data.get("decorations", []),
            option_a_image=question_data.get("btn_a_src", ""),
            option_b_image=question_data.get("btn_b_src", ""),
            option_c_image=question_data.get("btn_c_src", ""),
        )
        self.current_question.call_screen()
        self.current_question.bind(on_complete=self._next_question)
        self.base_layout.add_widget(self.current_question)

    def _next_question(self, instance, is_correct, value, elapsed_time):
        """Process the results of the current question and move to the next."""
        self.questions_cache.append(
            {
                "score": 20 if is_correct else 0,
                "value": value,
                "elapsed_time": elapsed_time,
                "timestamp": Clock.get_time(),
            }
        )

        if self.is_quiz_complete():
            self._finish_quiz()
        else:
            self.current_question_index += 1
            self._next_schedule = Clock.schedule_once(
                lambda dt: self._show_question(), 2
            )

    def restart_quest(self):
        """Restart the quiz from the beginning."""

        self._reset_screen_layout()
        self._reset_cache()

        self.current_question_index = 0
        self._show_question()

    def on_pre_enter(self, *args):
        """Prepare the screen when it is about to be displayed."""

        self.app.stop_backsound()
        self.current_question_index = 0
        self._show_question()
        return super().on_pre_enter(*args)

    def on_pre_leave(self, *args):
        """Stop the timer when the screen is about to be left."""

        if not self.app.configs_manager.get("mute"):
            self.app.play_backsound()

        if self._next_schedule:
            self._next_schedule.cancel()
            self._next_schedule = None

        if self.current_question:
            self.current_question.stop_quest()
            self.base_layout.remove_widget(self.current_question)
            self.current_question = None

        if self.finish:
            self.base_layout.remove_widget(self.finish)
            self.finish = None

        self._reset_cache()
        return super().on_pre_leave(*args)

    def _finish_quiz(self):
        """Display the finish screen with the final points."""

        total_score = sum(question["score"] for question in self.questions_cache)
        total_remaining_time = Clock.get_time() - self.start_time
        self.app.score_manager.save_score(
            self._group_key_store, self._key_store, total_score, total_remaining_time
        )

        self.finish = LayoutFinish(
            app=self.app,
            group_key_store=self._group_key_store,
            key_store=self._key_store,
            destination=self._home_destination,
        )

        self.finish.bind(on_go_home=lambda *args: self.on_pre_leave())
        self.finish.bind(on_restart_quest=lambda *args: self.restart_quest())

        self.base_layout.add_widget(self.finish)
