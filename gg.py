import json
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from calendar import monthrange
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from datetime import datetime
from kivy.lang import Builder

Window.size = (400, 540)

# Load the KV file
Builder.load_file('planner5.kv')

class WhiteSquareLabel(Widget):
    pass

class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.month_dropdown = DropDown()
        self.months = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        for month in self.months:
            month_btn = Button(
                text=month,
                size_hint_y=None,
                height=40,
                background_color=(0, 0, 0, 1),  # Black color for background
                color=(1, 1, 1, 1)  # White color for text
            )
            month_btn.bind(on_release=self.on_month_button_press)
            self.month_dropdown.add_widget(month_btn)

    def open_month_dropdown(self, instance):
        self.month_dropdown.open(instance)

    def on_month_button_press(self, instance):
        self.month_dropdown.dismiss()
        month = instance.text
        self.ids.month_label.text = f"Mês selecionado: {month}"
        month_index = self.months.index(month) + 1
        year = 2024
        num_days = monthrange(year, month_index)[1]
        self.ids.days_layout.clear_widgets()
        for day in range(1, num_days + 1):
            day_button = Button(
                text=str(day),
                size_hint=(None, None),
                size=(40, 40),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1)
            )
            day_button.bind(on_release=self.on_day_button_press)
            self.ids.days_layout.add_widget(day_button)
        self.ids.days_layout.opacity = 1

    def on_day_button_press(self, instance):
        selected_day = instance.text
        selected_month = self.ids.month_label.text.split(": ")[1]
        PlannerApp.get_running_app().selected_date = f"{selected_day} de {selected_month}"
        PlannerApp.get_running_app().screen_manager.current = "planner_screen"

class PlannerScreen(Screen):
    def on_pre_enter(self):
        selected_date = PlannerApp.get_running_app().selected_date
        self.ids.planner_label.text = f"Metas para {selected_date}"
        self.load_goals()

    def save_goals(self, instance):
        goals = self.ids.text_input.text
        selected_date = PlannerApp.get_running_app().selected_date
        self.store_goals(selected_date, goals)
        PlannerApp.get_running_app().screen_manager.current = "calendar_screen"

    def go_back(self, instance):
        PlannerApp.get_running_app().screen_manager.current = "calendar_screen"

    def store_goals(self, date, goals):
        data = self.load_all_goals()
        data[date] = goals
        with open('goals.json', 'w') as f:
            json.dump(data, f)

    def load_all_goals(self):
        try:
            with open('goals.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def load_goals(self):
        selected_date = PlannerApp.get_running_app().selected_date
        data = self.load_all_goals()
        self.ids.text_input.text = data.get(selected_date, "")

class PlannerApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(CalendarScreen(name="calendar_screen"))
        self.screen_manager.add_widget(PlannerScreen(name="planner_screen"))
        self.selected_date = None
        return self.screen_manager

if __name__ == '__main__':
    PlannerApp().run()
