import kivy

kivy.logger.Logger.setLevel("DEBUG")

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from app.screen.main_menu import MainMenu


class NadaCilikApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="main_menu"))
        return sm


if __name__ == "__main__":
    NadaCilikApp().run()
