from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CostCalculator(App):
    def build(self):
        self.title = "Vorwärts- und Rückwärtskalkulationsrechner"

        root_layout = GridLayout(cols=2, spacing=10, padding=10)

        # Labels und Eingabefelder für die Kosten und Produktionsmenge
        root_layout.add_widget(Label(text="Fixe Kosten:"))
        self.fixed_cost_input = TextInput(hint_text="1000", input_filter="float")
        root_layout.add_widget(self.fixed_cost_input)

        root_layout.add_widget(Label(text="Variable Kosten pro Einheit:"))
        self.variable_cost_input = TextInput(hint_text="15", input_filter="float")
        root_layout.add_widget(self.variable_cost_input)

        root_layout.add_widget(Label(text="Produktionsmenge:"))
        self.production_quantity_input = TextInput(hint_text="100", input_filter="int")
        root_layout.add_widget(self.production_quantity_input)

        root_layout.add_widget(Label(text="Gewinnmarge (%):"))
        self.profit_margin_input = TextInput(hint_text="20", input_filter="float")
        root_layout.add_widget(self.profit_margin_input)

        # Buttons zum Berechnen der Kosten und Verkaufspreise
        forward_button = Button(text="Vorwärtskalkulation")
        forward_button.bind(on_press=self.calculate_forward)
        root_layout.add_widget(forward_button)

        backward_button = Button(text="Rückwärtskalkulation")
        backward_button.bind(on_press=self.calculate_backward)
        root_layout.add_widget(backward_button)

        # Ergebnisanzeige
        self.result_label = Label(text="", size_hint=(None, None))
        root_layout.add_widget(self.result_label)

        return root_layout

    def calculate_forward(self, instance):
        try:
            fixed_costs = float(self.fixed_cost_input.text)
            variable_cost_per_unit = float(self.variable_cost_input.text)
            production_quantity = int(self.production_quantity_input.text)
        except ValueError:
            self.result_label.text = "Fehler: Bitte geben Sie gültige Zahlen ein."
            return

        total_costs = fixed_costs + (variable_cost_per_unit * production_quantity)
        cost_per_unit = total_costs / production_quantity

        result_text = f"Herstellungskosten pro Einheit: {cost_per_unit:.2f} EUR"

        self.result_label.text = result_text

    def calculate_backward(self, instance):
        try:
            fixed_costs = float(self.fixed_cost_input.text)
            variable_cost_per_unit = float(self.variable_cost_input.text)
            profit_margin = float(self.profit_margin_input.text)
        except ValueError:
            self.result_label.text = "Fehler: Bitte geben Sie gültige Zahlen ein."
            return

        required_profit_margin = profit_margin / 100
        min_price_per_unit = (fixed_costs / required_profit_margin + variable_cost_per_unit)

        result_text = f"Mindestverkaufspreis pro Einheit: {min_price_per_unit:.2f} EUR"

        self.result_label.text = result_text

if __name__ == "__main__":
    CostCalculator().run()
