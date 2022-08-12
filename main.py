#turotial: https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6&ab_channel=Codemy.com

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# For images
#from kivy.uix.image import Image
# Float latout
#from kivy.uix.floatlayout import Float

Builder.load_file('calc.kv')


# pyinstaller main.py
# to create .exe file

if __name__ != '__main__':
    exit()

# START OF PROGRAM

class MyLayout(Widget):
    def press(self):
        #ids is for referens to ID!!
        name = self.ids.name_input.text

        #update the label
        self.ids.name_label.text = name

class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1)
        return MyLayout()

# Set size of window
Window.size = (500,700)
CalculatorApp().run()
