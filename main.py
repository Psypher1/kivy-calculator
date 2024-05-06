import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.0")


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()


class PyCalculator(App):
    def build(self):
        return MyRoot()


if __name__ == "__main__":
    PyCalculator().run()
