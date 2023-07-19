from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QPushButton, QLineEdit, QWidget, QTextEdit, QHBoxLayout, QAction, QMenu
from PyQt5.QtCore import Qt
import random

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.todo_list = []
        self.responses = []  # Empty list for now

        self.motivational_responses = [
            "You did an excellent job!",
            "Well done on your accomplishment!",
            "Great job, keep up the good work!",
            "That's fantastic, you should be proud!",
            "Your work is truly impressive!",
            "Superb job, keep it up!",
            "Wonderful work, you're doing great!",
            "Outstanding performance, keep it going!",
            "Bravo! You're doing an amazing job!",
            "Terrific work, keep pushing forward!",
            "Amazing effort, you're making great progress!",
            "Awesome work, keep it up!",
            "Stellar performance, keep shining!",
            "Remarkable job, keep up the good work!",
            "Splendid work, you're doing fantastic!",
            "Marvelous effort, you're on the right track!",
            "Admirable work, keep it up!",
            "Phenomenal job, you're doing exceptionally well!",
            "Exceptional work, keep exceeding expectations!",
            "Your work is truly magnificent!"
        ]

        self.snarky_responses = [
            "Oh great, another thing for you to procrastinate on.",
            "Sure, like you're actually going to get it done.",
            "Adding tasks to your to-do list won't magically make you productive.",
            "Haha, good luck with that one.",
            "You're just giving yourself more things to stress about.",
            "Adding tasks is easy. Completing them? That's another story.",
            "Why bother? You're just going to forget about it anyway.",
            "Your to-do list keeps growing, but your productivity doesn't.",
            "Here's another task for you to ignore.",
            "Sure, let's see how long it stays on your list.",
            "Adding tasks won't make you more organized. It'll just clutter your list.",
            "Oh look, another meaningless task for you to ignore.",
            "Adding tasks is the easy part. Getting them done? Not so much.",
            "Don't worry, procrastination is an art form.",
            "Sure, just keep adding tasks instead of actually doing them.",
            "You're really good at making to-do lists. Actually doing the tasks? Not so much.",
            "Ah, the never-ending cycle of adding tasks and never completing them.",
            "Adding tasks won't make you productive. Taking action will.",
            "Sure, let's add more tasks to the never-ending abyss.",
            "Congratulations, you've just given yourself more things to feel guilty about."
        ]

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.v_layout = QVBoxLayout()
        self.layout.addLayout(self.v_layout)

        self.list_widget = QListWidget()
        self.v_layout.addWidget(self.list_widget)

        self.entry = QLineEdit()
        self.v_layout.addWidget(self.entry)

        self.add_button = QPushButton('Add Item')
        self.add_button.clicked.connect(self.add_item)
        self.v_layout.addWidget(self.add_button)

        self.remove_button = QPushButton('Remove Item')
        self.remove_button.clicked.connect(self.remove_item)
        self.v_layout.addWidget(self.remove_button)

        self.settings_button = QPushButton("Settings")
        self.settings_button.setMenu(self.create_settings_menu())  # Create and set the settings menu
        self.v_layout.addWidget(self.settings_button)

        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)
        self.layout.addWidget(self.response_box)

        self.dark_theme = False

        self.switch_theme()  # Set initial theme to dark

        self.setGeometry(200, 200, 800, 400)  # Sets initial window size
        self.show()

        self.entry.setFocus()  # Set focus on the text box
        self.entry.returnPressed.connect(self.add_item)

        self.set_mode("Motivational")  # Set default response mode to motivational

    def create_settings_menu(self):
        settings_menu = QMenu()

        motivational_action = QAction("Motivational", self)
        motivational_action.setCheckable(True)
        motivational_action.setChecked(True)  # Set Motivational as the default mode
        motivational_action.triggered.connect(lambda: self.set_mode("Motivational"))

        snarky_action = QAction("Snarky", self)
        snarky_action.setCheckable(True)
        snarky_action.triggered.connect(lambda: self.set_mode("Snarky"))

        settings_menu.addAction(motivational_action)
        settings_menu.addAction(snarky_action)

        return settings_menu

    def set_mode(self, mode):
        if mode == "Motivational":
            self.responses = self.motivational_responses
            self.settings_button.menu().actions()[1].setChecked(False)  # Uncheck Snarky mode
        elif mode == "Snarky":
            self.responses = self.snarky_responses
            self.settings_button.menu().actions()[0].setChecked(False)  # Uncheck Motivational mode

        if self.responses:
            self.response_box.append(random.choice(self.responses))  # Display initial response

    def add_item(self):
        item = self.entry.text()
        if item:
            self.todo_list.append(item)
            self.update_list_widget()
            self.entry.clear()
            if self.responses:
                self.response_box.append(random.choice(self.responses))
            self.list_widget.setCurrentRow(len(self.todo_list) - 1)  # Select the last item
            self.entry.setFocus()  # Set focus on the text box after adding an item
        else:
            self.response_box.append("You must enter a task.")
            self.entry.setFocus()  # Set focus on the text box if no item was entered

    def remove_item(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.todo_list.remove(item.text())
                self.response_box.append(f'"{item.text()}" removed from the to-do list!')

            self.update_list_widget()
            self.entry.setFocus()  # Set focus on the text box after removing item(s)
        else:
            self.response_box.append("You must select a task.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.remove_item()

    def update_list_widget(self):
        self.list_widget.clear()
        self.list_widget.addItems(self.todo_list)

    def switch_theme(self):
        self.dark_theme = not self.dark_theme
        if self.dark_theme:
            self.setStyleSheet("""
                QWidget {
                    background-color: #323232;
                    color: #ffffff;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #ffffff;
                    color: #000000;
                }
            """)

if __name__ == "__main__":
    app = QApplication([])
    window = ToDoApp()
    app.exec_()
