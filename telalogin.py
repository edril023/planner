from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder

def resize_window(*args):
    Window.size = (357, 550)

class WhiteSquare(Widget):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class ClickableLabel(ButtonBehavior, Label):
    pass

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)
        return Builder.load_file('planner2.kv')

    def toggle_password_visibility(self):
        peso_input = self.root.ids.peso_input
        toggle_button = self.root.ids.toggle_button
        peso_input.password = not peso_input.password
        toggle_button.source = 'fechado.png' if peso_input.password else 'aberto.png'

    def forgot_password(self):
        print("vai pra outra tela")

if __name__ == '__main__':
    Window.size = (400, 400)
    Window.bind(on_resize=resize_window)
    PlannerApp().run()
