from kaki.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
import os
from Screens.RootScreen.root_screen import RootScreen
from Screens.HomeScreen.home_screen import HomeScreen
from Screens.EncodeScreen.encode_screen import EncodeScreen
from Screens.EmbedScreen.embed_screen import EmbedScreen

import kivymd
Window.size = (310, 580)


class EndeApp(App, MDApp):
    KV_FILES = {
        os.path.join(os.getcwd(), "Screens/RootScreen/root_screen.kv"),
        os.path.join(os.getcwd(), "Screens/HomeScreen/home_screen.kv"),
        os.path.join(os.getcwd(), "Screens/EmbedScreen/embed_screen.kv"),
        os.path.join(os.getcwd(), "Screens/EncodeScreen/encode_screen.kv")
    }

    CLASSES = {
        "RootScreen": "root_screen",
        "HomeScreen": "home_screen",
        "EmbedScreen": "embed_screen",
        "EncodeScreen": "encode_screen",
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        return RootScreen();

EndeApp().run();