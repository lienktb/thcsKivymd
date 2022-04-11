from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivy.utils import get_color_from_hex
from plyer import filechooser
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout

class ModalContent(MDBoxLayout):
    pass

class EncodeScreen(MDScreen):
    title = "Upload Text"
    dialog = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.manager = None

    def file_manager_open(self):
        path = "";
        file = filechooser.open_file();
        if(file):
            path = file[0]
            self.ids.link_file.text = path
            f = open(path, "r");
            self.ids.textContent.text = f.read();
            print(f.read());

        else:
            return;

    def read_file(self):
        link_file = self.ids.link_file.text;

        if(link_file!=""):
            path = link_file
            f = open(path, "r");
            self.ids.textContent.text = f.read();
            print(f.read());
        else:
            self.show_error()


    def show_error(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=ModalContent(),
            )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()