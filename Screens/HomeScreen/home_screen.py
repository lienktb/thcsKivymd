from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase;
from kivymd.uix.floatlayout import MDFloatLayout
import io
import os
class Tab(MDFloatLayout, MDTabsBase):
    # path = os.path.join(os.getcwd(), "assets/data/encode.txt")
    f = open("F:/PythonKivy/navbar/assets/data/encode.txt", encoding="utf8")
    content_text = f.read();
    f.close()


class HomeScreen(MDScreen):
    content_text = "Apple"
    def on_tab_switch(self, *args):
        tab_text = args[3]
        instance_tabs = args[1]
        print(f'Now on tab: {tab_text}')
        self.content_text = tab_text
        if tab_text == 'Mã hóa':
            result = self.read_file("encode.txt");
            instance_tabs.ids.label.text = result
        elif tab_text == 'RSA':
            result = self.read_file("rsa.txt");
            instance_tabs.ids.label.text = result

        elif tab_text == 'LSB':
            result = self.read_file("lsb.txt");
            instance_tabs.ids.label.text = result

    def read_file(self, file):
        # path = os.path.join(os.getcwd(), "assets/data/"+file)
        f = io.open("F:/PythonKivy/navbar/assets/data/"+file, mode="r", encoding="utf-8")
        result = f.read();
        f.close()
        return result;
