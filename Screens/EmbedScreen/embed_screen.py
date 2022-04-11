from kivymd.uix.screen import MDScreen

from plyer import filechooser
class EmbedScreen(MDScreen):
    title = "Upload Image"
    def file_manager_open(self):
        path = filechooser.open_file()[0]
        # this method returns a list with the first index
        # being the path of the file selected
        self.ids.link_file.text = path
        image_name = path.split('/')[-1]
        self.ids.image.source = image_name

        print(image_name)