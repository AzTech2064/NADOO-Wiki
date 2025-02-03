"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class hellocamera(toga.App):
    def startup(self):
        main_box = toga.Box()

        self.photo = toga.ImageView(style = Pack(height = 300, padding = 5))
        camera_button = toga.Button(
            "Take photo",
            on_press = self.take_photo,
            style = Pack(padding = 5)
        )
        
        main_box.add(self.photo)
        main_box.add(camera_button)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    async def take_photo(self, widget, **kwargs):
        try:
            if not self.camera.has_permission:
                await self.camera.request_permission()
                
            image = await self.camera.take_photo()
            if image:
                self.photo.image = image
        except NotImplementedError:
            await self.main_window.dialog(
                toga.InfoDialog(
                    "Oh no!",
                    "The Camera API is not implemented on this platform",
                )
            )
        except PermissionError:
            await self.main_window.dialog(
                toga.InfoDialog(
                    "Oh no!",
                    "You have not granted permission to take photos",
                )
            )


def main():
    return hellocamera()
