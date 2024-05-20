from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
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

class ImageButton(ButtonBehavior, Image):
    pass

class ClickableLabel(ButtonBehavior, Label):
    pass

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
            hint_text="email ou nome de usuario", font_size=16, multiline=False, size_hint=(None, None),
            size=(280, 40), foreground_color=(0, 0, 0, 1), cursor_color=(1, 1, 0, 1), background_color=(1, 0.8, 0.6, 1)
        )
        self.altura_input.pos_hint = {'center_x': 0.64, 'center_y': 1.4}

        self.peso_input = TextInput(
            hint_text="senha", font_size=16, multiline=False, password=True, size_hint=(None, None),
            size=(280, 40), foreground_color=(0, 0, 0, 1), cursor_color=(1, 1, 0, 1), background_color=(1, 0.8, 0.6, 1)
        )
        self.peso_input.pos_hint = {'center_x': 0.64, 'center_y': 1.2}

        # Create ImageButton to show/hide password
        self.toggle_button = ImageButton(
            source='fechado.png', size_hint=(None, None), size=(25, 25),
            pos_hint={'center_x': 0.97, 'center_y': 1.2}, on_press=self.toggle_password_visibility
        )

        # Create Button
        self.submit_button = Button(
            text="login", size_hint=(None, None), size=(150, 40),
            color=(0.5, 0.5, 0.5, 1), background_color=(1, 0.8, 0.6, 1)
        )
        self.submit_button.pos_hint = {'center_x': 0.83, 'center_y': 0.9}

        # Create clickable label for "Forgot Password"
        self.forgot_password_label = ClickableLabel(
            text="Esqueci minha senha", size_hint=(None, None), size=(150, 20),
            pos_hint={'center_x': 0.40, 'center_y': 0.9}, color=(1, 0.65, 0.4), font_size=13
        )
        self.forgot_password_label.bind(on_press=self.forgot_password)

        # Add TextInput fields, ImageButton, Button, and ClickableLabel to the layout
        input_layout.add_widget(self.altura_input)
        input_layout.add_widget(self.peso_input)
        input_layout.add_widget(self.toggle_button)
        input_layout.add_widget(self.submit_button)
        input_layout.add_widget(self.forgot_password_label)

        # Add input_layout to white_square
        white_square.add_widget(input_layout)

        return layout

    def toggle_password_visibility(self, instance):
        self.peso_input.password = not self.peso_input.password
        if self.peso_input.password:
            self.toggle_button.source = 'fechado.png'
        else:
            self.toggle_button.source = 'aberto.png'

    def forgot_password(self, instance):
        print("vai pra outra tela")

if __name__ == '__main__':
    Window.size = (400, 400)
    Window.bind(on_resize=resize_window)
    PlannerApp().run()