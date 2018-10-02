from kivy.app import App
from kivy.lang import Builder

MILES_to_KM = 1.60934


class ConversionApp(App):
    def build(self):
        self.title = 'Converting App'
        self.root = Builder.load_file('converting_distances.kv')
        return self.root

    def handle_calculations(self):
        value = self.error_check_input()
        result = value * MILES_to_KM
        self.root.ids.output_label.text = str(result)

    def error_check_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increments(self, change):
        value = self.error_check_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculations()


ConversionApp().run()
