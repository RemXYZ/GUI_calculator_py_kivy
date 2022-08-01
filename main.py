#turotial: https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6&ab_channel=Codemy.com

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# pyinstaller main.py
# to create .exe file

if __name__ != '__main__':
    exit()

# START OF PROGRAM

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        #Add widgets
        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline = False)
        self.add_widget(self.name)


        self.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=True)
        self.add_widget(self.pizza)


class MyApp(App):
    def build(self):
        return MyGridLayout()


MyApp().run()