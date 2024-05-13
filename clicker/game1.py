from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class ClickerApp(App):
    count = 0
    cps = 0  # Clicks per second

    def __init__(self, **kwargs):
        super(ClickerApp, self).__init__(**kwargs)
        self.upgrades = {
            "Рука": {"base_cost": 100, "cps": 1, "purchased": 0, "cost_increase_factor": 1.1},
            "Бендер": {"base_cost": 1500, "cps": 10, "purchased": 0, "cost_increase_factor": 1.2},
            "Мегамен": {"base_cost": 99999, "cps": 99999, "purchased": 0, "cost_increase_factor": 1.3},
            "Чіт": {"base_cost": 1, "cps": 9**10, "purchased": 0, "cost_increase_factor": 1.3}
        }


    def build(self):


        self.window = GridLayout(cols=2)

        self.label = Label(text=self.update_text(), font_size=18, pos_hint="center", color="#B8B8B8")
        self.window.add_widget(self.label)


        self.info = Label(text='ESC = Закрити програму', font_size=18, pos_hint="center", color="#2F60B5")
        self.window.add_widget(self.info)


        self.button = Button(text="Тиц", bold=True, size_hint=(0.1, 0.2))
        self.button.bind(on_press=self.add_clicks)
        self.window.add_widget(self.button)



        for name in self.upgrades:
            btn = Button(text=f"Купити {name}", size_hint=(0.1, 0.1))
            btn.bind(on_press=lambda instance, x=name: self.purchase_upgrade(x))
            self.window.add_widget(btn)


        Clock.schedule_interval(self.update_cps, 1)

        return self.window

    def update_cps(self, dt):
        self.count += self.cps
        self.label.text = self.update_text()

    def add_clicks(self, instance):
        self.count += 1  # Default increment is 1 click per press
        self.label.text = self.update_text()

    def purchase_upgrade(self, upgrade_name):
        upgrade = self.upgrades[upgrade_name]
        current_cost = int(upgrade['base_cost'] * (upgrade['cost_increase_factor'] ** upgrade['purchased']))
        if self.count >= current_cost:
            self.count -= current_cost
            self.cps += upgrade['cps']
            upgrade['purchased'] += 1
            self.info.text = f'{upgrade_name} куплено {upgrade["purchased"]} раз! Поточний CPS: {self.cps}'
        else:
            self.info.text = 'Не достатньо кліків для купівля'
        self.label.text = self.update_text()

    def update_text(self):
        return (f"Ти наклікав цілих {self.count:,} раз"
                f"\nПоточний CPS: {self.cps}"
                f"\nВартість 'Рука' : {int(self.upgrades['Рука']['base_cost'] * (self.upgrades['Рука']['cost_increase_factor'] ** self.upgrades['Рука']['purchased']))}"
                f"\nВарість 'Бендер' : {int(self.upgrades['Бендер']['base_cost'] * (self.upgrades['Бендер']['cost_increase_factor'] ** self.upgrades['Бендер']['purchased']))}"
                f"\nВарість 'Мегамен' : {int(self.upgrades['Мегамен']['base_cost'] * (self.upgrades['Мегамен']['cost_increase_factor'] ** self.upgrades['Мегамен']['purchased']))}")

if __name__ == "__main__":
    ClickerApp().run()
