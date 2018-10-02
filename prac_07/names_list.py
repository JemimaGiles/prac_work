"""Kivy attempt at displaying a list/dictionary in labels"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window

NAMES = ["Jim", "Pam", "Dwight", "Michael", "Kelly", "Angela"]


class NamesListApp(App):

    def build(self):
        self.title = 'The Office'
        self.root = Builder.load_file('names_list.kv')
        Window.size = (500, 200)
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in NAMES:
            names_box = Label(text=name)
            self.root.ids.names_box.add_widget(names_box)


NamesListApp().run()
