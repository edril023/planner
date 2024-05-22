from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder

class PlannerLayout(FloatLayout):
    pass

class PlannerApp(App):
    def build(self):
        # Set the background color of the window to be transparent
        Window.clearcolor = (0, 0, 0, 0)
        # Load the .kv file
        return PlannerLayout()

if __name__ == '__main__':
    # Set the initial window size
    Window.size = (357, 550)
    PlannerApp().run()
