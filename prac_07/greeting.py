from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class GreetingDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('greeting.kv')
        Window.size = (500, 200)
        return self.root

    def handle_greet(self):
        # print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


GreetingDemo().run()
