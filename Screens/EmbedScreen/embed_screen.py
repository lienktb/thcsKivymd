from kivymd.uix.screen import MDScreen
import base64
from plyer import filechooser
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
import requests
import json

class ModalSuccess(MDBoxLayout):
    pass
class ModalContent(MDBoxLayout):
    pass
class EmbedScreen(MDScreen):
    title = "Upload Image"
    path = "";
    dialog = None
    media = {};
    message="";
    def file_manager_open(self):

        file = filechooser.open_file();
        if(file):
            self.path = file[0]
            print("hello")
            # this method returns a list with the first index
            # being the path of the file selected
            f = open(self.path, "rb");
            image = open(self.path, "rb");
            self.media = {"file": image}
            # self.image_b64 = base64.b64encode(image).decode("utf8");
            # print("b64: ", self.image_b64)
            self.ids.link_file.text =  self.path
            image_name =  self.path.split('/')[-1]
            self.ids.image.source = image_name
        else:
            return;

    def embedwtm(self):
        if (self.media):
            req = requests.post('http://localhost:8080/wtfile',  files=self.media);
            res = json.loads(req.text);
            img_data = requests.get(res["text"]).content
            with open(self.path, 'wb') as f:
                f.write(img_data);
                f.close();
            print(self.path)
            self.ids.link_file.text = self.path
            image_name = self.path.split('/')[-1]
            self.ids.image.reload();
        else:
            self.show_error()

    def show_error(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=ModalContent(),
            )
        self.dialog.open()

    def embedLsb(self):
        if(self.ids.message.text):
            self.message = self.ids.message.text;
        if(len(self.message) !=0 and self.media):
            req = requests.post('http://localhost:8080/encryptLsb',  files=self.media, data={"text": self.message});
            res = json.loads(req.text);
            img_data = requests.get(res["text"]).content
            with open(self.path, 'wb') as f:
                f.write(img_data);
                f.close();
            self.ids.message.text = ""
            self.message = ""
            self.ids.link_file.text = self.path
            self.ids.image.reload();
            self.show_success()
        else:
            self.show_error();

    def decryptLsb(self):
        f = open(self.path, "rb");
        image = open(self.path, "rb");
        self.media = {"file": image}
        if(self.media):
            try:
                req = requests.post('http://localhost:8080/decryptLsb', files=self.media);
                res = json.loads(req.text);
                if(res):
                    print(res["text"]);
                    self.ids.message.text = res["text"]
            except:
                self.show_error();
    def close_dialog(self):
        self.dialog.dismiss();
    def show_success(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=ModalSuccess(),
            )
        self.dialog.open()
    def showResult(self, req, result):
        # print(result);
        print("hello");
        # self.text = result['text'];
        # self.writeFile(result['text'])
        # self.ids.textContent.text = result['text'];