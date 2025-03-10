from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class TodoApp(App):
    def build(self):
        Window.size = (400, 600)

        self.main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        title_label = Label(
            text="TODO List", font_size=24, size_hint=(1, 0.1), bold=True
        )
        self.main_layout.add_widget(title_label)

        self.task_input = TextInput(
            hint_text="Enter task here...", multiline=False, size_hint=(1, 0.1)
        )
        self.main_layout.add_widget(self.task_input)

        add_button = Button(
            text="Add Todo", size_hint=(1, 0.1), background_color=(0, 0.7, 0, 1)
        )
        add_button.bind(on_press=self.add_task)
        self.main_layout.add_widget(add_button)

        self.task_list = ScrollView(size_hint=(1, 0.7))
        self.tasks_layout = BoxLayout(
            orientation="vertical", spacing=5, size_hint_y=None
        )
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter("height"))
        self.task_list.add_widget(self.tasks_layout)
        self.main_layout.add_widget(self.task_list)

        return self.main_layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()

        if task_text:
            task_widget = BoxLayout(size_hint_y=None, height=40, spacing=5)
            task_label = Button(
                text=task_text, size_hint_x=0.8, color=(0.5, 0.8, 0.8, 1)
            )
            delete_button = Button(
                text="X", size_hint_x=0.2, background_color=(1, 0, 0, 1)
            )
            delete_button.bind(
                on_press=lambda btn, lbl=task_label: self.delete_task(lbl)
            )

            task_widget.add_widget(task_label)
            task_widget.add_widget(delete_button)

            self.tasks_layout.add_widget(task_widget)

            self.task_input.text = ""

    def delete_task(self, label):
        for task in self.tasks_layout.children:
            if label in task.children:
                self.tasks_layout.remove_widget(task)
                break


if __name__ == "__main__":
    TodoApp().run()
