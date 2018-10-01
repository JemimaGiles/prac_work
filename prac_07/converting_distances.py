from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertDistancesApp(App):

    def build(self):
        self.title = 'Convert miles to kilometers'
        self.root = Builder.load_file('converting_distances.kv')
        return self.root

    def handle_conversion(self):
        value = self.error_check()
        result = value * MILES_TO_KM
        self.root.ids.output_lable.text = str(result)

    def handle_increment(self, change):
        value = self.error_check() + change
        self.root.ids.input_number.text = str(value)
        self.handle_conversion()

    def error_check(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertDistancesApp().run()
