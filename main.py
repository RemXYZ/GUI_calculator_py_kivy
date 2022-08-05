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
        self.cols = 1

        #Second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #Add widgets
        self.top_grid.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline = False)
        self.top_grid.add_widget(self.name)


        self.top_grid.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=True)
        self.top_grid.add_widget(self.pizza)

        # The new top_grid to our app
        self.add_widget(self.top_grid)


        # submit button
        self.submit = Button(text="Submit", font_size=32)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        

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
