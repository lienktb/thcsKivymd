from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivy.utils import get_color_from_hex
from plyer import filechooser
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.network.urlrequest import UrlRequest
import requests
import json

class ModalContent(MDBoxLayout):
    pass

class EncodeScreen(MDScreen):
    title = "Upload Text"
    text = ""
    dialog = None
    path = "";
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.manager = None

    def file_manager_open(self):

        file = filechooser.open_file();
        if(file):
            self.path = file[0]
            self.ids.link_file.text = self.path
            f = open(self.path, "r");
            self.text = f.read();
            self.ids.textContent.text = self.text;

            # print(f.read());
            f.close()
        else:
            return;

    def read_file(self):
        link_file = self.ids.link_file.text;

        if(link_file!=""):
            path = link_file
            f = open(path, "r");
            self.ids.textContent.text = f.read();
            f.close();
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

    def encode(self):
        if(self.text):
            print(self.text)
            data = {"text": self.text};
            headers = {'Content-Type': 'application/json'}
            req = requests.post('http://localhost:8080/encryptText', data=json.dumps(data), headers=headers);
            res = json.loads(req.text);
            if (res):
                self.showResult(res);
        else:
            self.show_error()
        # print("ma hoa");
    def showResult(self, result):

        print(result['text']);
        self.text = result['text'];
        self.writeFile(result['text'])
        self.ids.textContent.text = result['text'];

    def writeFile(self, result):
        f = open(self.path, "w");
        f.write(result);
        f.close();

    def decode(self):
        if(self.text):
            print(self.text);
            data = {"text": self.text};
            headers = {'Content-Type': 'application/json'}
            req = requests.post('http://localhost:8080/decryptTextPV', data=json.dumps(data), headers=headers);
            res = json.loads(req.text);
            if (res):
                self.showResult(res);
            print(res)
        else:
            self.show_error();
    #
    # def showResultDecode(self, req, result):
    #     print(result["text"])
