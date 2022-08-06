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

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text

        #print(f"Hello {name} your favorite pizza is {pizza}")
        # print it to the screen
        self.add_widget(Label(text=f"Hello {name} your favorite pizza is {pizza}"))


class MyApp(App):
    def build(self):
        return MyGridLayout()


MyApp().run()
