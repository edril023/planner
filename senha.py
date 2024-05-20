from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import RoundedRectangle

def resize_window(*args):
    Window.size = (357, 550)

class WhiteSquare(Widget):
    def __init__(self, **kwargs):
        super(WhiteSquare, self).__init__(**kwargs)
        with self.canvas:
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)

        # Create the main layout
        layout = FloatLayout()

        # Add background image
        background = Image(source="fundo3.jpeg", size_hint=(None, None), size=(700,1000),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        # Add white square overlay
        white_square = WhiteSquare(size_hint=(None, None), size=(320, 270))
        white_square.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(white_square)

        # FloatLayout to hold TextInput fields and Button inside WhiteSquare
        input_layout = FloatLayout(size_hint=(None, None), size=(350, 300))

        # Create TextInput fields
        self.altura_input = TextInput(
            hint_text="insira senha nova", font_size=16, multiline=False, size_hint=(None, None),
            size=(280, 40), foreground_color=(0, 0, 0, 1), cursor_color=(1, 1, 0, 1), background_color=(1, 0.8, 0.6, 1)
        )
        self.altura_input.pos_hint = {'center_x': 0.64, 'center_y': 1.4}

        self.peso_input = TextInput(
            hint_text="confirme a senha", font_size=16, multiline=False, password=True, size_hint=(None, None),
            size=(280, 40), foreground_color=(0, 0, 0, 1), cursor_color=(1, 1, 0, 1), background_color=(1, 0.8, 0.6, 1)
        )
        self.peso_input.pos_hint = {'center_x': 0.64, 'center_y': 1.2}

        # Create Button
        self.confirm_button = Button(
            text="confirmar", size_hint=(None, None), size=(150, 40),
            color=(0.5, 0.5, 0.5, 1), background_color=(0.87, 0.63, 0.87)  # Cor alterada para azul claro
        )
        self.confirm_button.pos_hint = {'center_x': 0.64, 'center_y': 0.9}

        # Add TextInput fields and Button to the layout
        input_layout.add_widget(self.altura_input)
        input_layout.add_widget(self.peso_input)
        input_layout.add_widget(self.confirm_button)

        # Add input_layout to white_square
        white_square.add_widget(input_layout)

        return layout

if __name__ == '__main__':
    Window.size = (400, 540)
    Window.bind(on_resize=resize_window)
    PlannerApp().run()