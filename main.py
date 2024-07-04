import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


def calculate_volume(width, length, height):
    """Вычисляет объем коробки в литрах."""
    return (width * length * height) / 1000


def calculate_silicone_weight(figure_weight, figure_density, box_volume):
    """Вычисляет вес силикона, необходимый для заливки, в кг."""
    figure_volume = figure_weight / figure_density
    silicone_volume = box_volume - figure_volume
    silicone_density = 1.1  # Плотность силикона (кг/л)
    return round(silicone_volume * silicone_density, 2)  # Округление до 2 знаков после запятой


class SiliconeCalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=5)

        # --- Поля ввода для коробки ---
        layout.add_widget(Label(text="Ширина коробки (см):"))
        self.box_width_input = TextInput(multiline=False)
        layout.add_widget(self.box_width_input)

        layout.add_widget(Label(text="Длина коробки (см):"))
        self.box_length_input = TextInput(multiline=False)
        layout.add_widget(self.box_length_input)

        layout.add_widget(Label(text="Высота коробки (см):"))
        self.box_height_input = TextInput(multiline=False)
        layout.add_widget(self.box_height_input)

        # --- Поля ввода для фигурки ---
        layout.add_widget(Label(text="Вес фигурки (г):"))
        self.figure_weight_input = TextInput(multiline=False)
        layout.add_widget(self.figure_weight_input)

        layout.add_widget(Label(text="Материал фигурки:"))
        self.figure_material_spinner = Spinner(
            text="Выберите материал",
            values=("Гипс", "Полистоун")
        )
        layout.add_widget(self.figure_material_spinner)

        # --- Кнопка расчета ---
        calculate_button = Button(text="Рассчитать")
        calculate_button.bind(on_press=self.calculate)
        layout.add_widget(calculate_button)

        # --- Метка для вывода результата ---
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        try:
            box_width = float(self.box_width_input.text)
            box_length = float(self.box_length_input.text)
            box_height = float(self.box_height_input.text)
            figure_weight = float(self.figure_weight_input.text) / 1000  # Перевод в кг
            figure_material = self.figure_material_spinner.text.lower()

            if figure_material == "гипс":
                figure_density = 2.3
            elif figure_material == "полистоун":
                figure_density = 1.9
            else:
                self.result_label.text = "Выберите материал фигурки."
                return

            box_volume = calculate_volume(box_width, box_length, box_height)
            silicone_weight = calculate_silicone_weight(figure_weight, figure_density, box_volume)

            self.result_label.text = f"Вес силикона: {silicone_weight:.2f} кг"

        except ValueError:
            self.result_label.text = "Введите корректные данные."


if __name__ == '__main__':
    SiliconeCalculatorApp().run()
