from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from plyer import vibrator
from kivy import platform

Window.size = (300, 500)
Builder.load_file('calc.kv')


def touch():
    if platform == 'android' or 'ios':
        vibrator.vibrate(0.1)


def ex():
    App.get_running_app().stop()


class MyLayout(Widget):
    calc_history = []

    def rem(self):
        prior = self.ids.calc_input.text
        if prior != "0":

            if len(prior) == 1:
                self.ids.calc_input.text = "0"
            else:
                prior = prior[:-1]
                self.ids.calc_input.text = prior

    def per(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'({prior}%)'

    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, Button):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{Button}'

        else:
            self.ids.calc_input.text = f'{prior}{Button}'

    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}x'

    def division(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    def equal(self):
        prior = self.ids.calc_input.text
        if "%" in prior:
            prior = self.ids.calc_input.text
            ans = 0.0
            if "x" in prior:
                prior = prior.replace('(', '').replace(')', '').replace('%', '')
                elist = prior.split("x")
                ans = float(elist[0]) * float(elist[1]) / 100
            self.ids.calc_input.text = str(ans)
        else:
            if "+" in prior or "-" in prior or "x" in prior or "/" in prior:
                prior = prior.replace("x", "*")
                ans = eval(prior)
                self.ids.calc_input.text = str(ans)


class calculatorApp(App):
    def build(self):
        self.icon = r'C:\Users\gopug\Downloads\calculator.png'
        return MyLayout()


if __name__ == '__main__':
    calculatorApp().run()
