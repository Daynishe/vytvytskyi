from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'First'
            on_press: root.manager.current = "first"
        Button:
            text: 'Second'
            on_press: root.manager.current = "second"
        Button:
            text: 'Third'
            on_press: root.manager.current = "third"
        Button:
            text: 'Quit'
            on_press: App.Exit()

<FirstScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: '1'
        Button:
            text: '2'
        Button:
            text: '3'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<SecondScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: '1'
        Button:
            text: '2'
        Button:
            text: '3'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<ThirdScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: '1'
        Button:
            text: '2'
        Button:
            text: '3'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")


class MenuScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))

        return sm


if __name__ == '__main__':
    TestApp().run()
