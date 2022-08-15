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

    def write_num(self, num):
        if num == ".":
            return

        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = ''

        if prior == "0":
            self.ids.calc_input.text = num
        else:
            self.ids.calc_input.text = prior + num

    def clear(self):
        self.ids.calc_input.text = '0'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = prior + "."
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = prior + "."

        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","+")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"


class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1)
        return MyLayout()

# Set size of window
Window.size = (500,700)
CalculatorApp().run()
