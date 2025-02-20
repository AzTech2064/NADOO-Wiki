"""
My first application
"""
import httpx
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def greeting(name):
    if name:
        if name == "Brutus":
            return "BeeWare the IDEs of Python!"
        else:
            return f"Hello, {name}"
    else:
        return "Hello, stranger"

class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        name_label = toga.Label(
            "Your Name: ",
            style = Pack(padding=(0, 5)), 
        )
        self.name_input = toga.TextInput(style = Pack(flex = 1))
        
        name_box = toga.Box(style = Pack(direction = ROW, padding = 5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        
        button = toga.Button(
            "Say Hallo!",
            on_press = self.say_hello,
            style = Pack(padding = 5),
        )
        
        main_box.add(name_box)
        main_box.add(button)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")
            
        payload = response.json()
        
        await self.main_window.dialog(
            toga.InfoDialog(
                greeting(self.name_input.value),
                payload["body"],
            )
        )
    
def main():
    return HelloWorld()
