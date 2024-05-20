from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window

def resize_window(*args):
    Window.size = (357, 550)

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)

        # Create the main layout
        layout = FloatLayout()

        # Add background image
        background = Image(source="fundo3.jpeg", size_hint=(None, None), size=(700, 1000),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        centered_image = Image(source="logo.png", size_hint=(None, None), size=(500, 500),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(centered_image)
        return layout

if __name__ == '__main__':
    Window.size = (357, 550)
    PlannerApp().run()
