import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 500)


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        self.calc_field.text += symbol


class PyCalculator(App):
    def build(self):
        return MyRoot()


if __name__ == "__main__":
    PyCalculator().run()
