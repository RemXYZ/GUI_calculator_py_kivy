#turotial: https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6&ab_channel=Codemy.com

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('inherit.kv')


# pyinstaller main.py
# to create .exe file

if __name__ != '__main__':
    exit()

# START OF PROGRAM

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()


AwesomeApp ().run()
