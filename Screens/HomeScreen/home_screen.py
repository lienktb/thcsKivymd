from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class HomeScreen(MDScreen):
    pass