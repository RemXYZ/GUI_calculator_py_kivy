#turotial: https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6&ab_channel=Codemy.com

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


# pyinstaller main.py
# to create .exe file

if __name__ != '__main__':
    exit()

# START OF PROGRAM

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)


    def press(self):
        name = self.name.text
        pizza = self.pizza.text

        #print(f"Hello {name} your favorite pizza is {pizza}")
        # print it to the screen
        #self.add_widget(Label(text=f"Hello {name} your favorite pizza is {pizza}"))
        print(f"Hello {name} and your favorite pizza is {pizza}")
        self.name.text = ""
        self.pizza.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


MyApp().run()
