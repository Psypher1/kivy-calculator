import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("1.9.0")


class PyCalculator(App):
    def build(self):
        return Label(text="Py Calc")


if __name__ == "__main__":
    PyCalculator().run()
