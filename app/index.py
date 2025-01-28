from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QCheckBox, QFrame
from gui.ui_main import Ui_Form as Ui_main  # Ensure the correct path to the UI file
from utils.JSONFileChangeMonitor import JsonFileChangeHandler
from watchdog.observers import Observer

import json, os, random, time

class MainWindow(QWidget, Ui_main):
    def __init__(self):
        # setup ui
        super().__init__()
        self.setupUi(self)
        
        # initialize .json file directory
        self.tasksDir = os.path.join(os.getcwd(), *["tasks.json"])
        # button connections
        self.buttonConnections()
        # load tasks table
        self.loadTasksTable()

    def jsonChangeHandler(self):
        """monitor changes on json file"""
        eventHandler = JsonFileChangeHandler(self.tasksDir)
        observer = Observer()
        observer.schedule(eventHandler, path=".", recursive=False)

        observer.start()
        print("JSON file change handler started")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping monitoring...")
            observer.stop()

        observer.join()

    def loadTasksTable(self):
        """Load the tasks table"""
        taskData = self.getData()

        scrollWidget = self.todo_scrollAreaWidgetContents

        # Step 1: Get the existing layout (if it exists)
        existing_layout = scrollWidget.layout()

        # Step 2: If a layout exists, clear the existing frames (widgets) from the layout
        if existing_layout is not None:
            for i in range(existing_layout.count()):
                item = existing_layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if isinstance(widget, QFrame):  # Remove only QFrame widgets
                        widget.deleteLater()  # Properly remove and delete the widget

        # Step 3: Add new QFrame widgets to the existing layout
        for data in taskData:
            if data["taskStatus"] == "complete":
                continue

            print(f"Received data from task table: {data}")
            # Initialize widgets
            taskCont = QFrame()
            taskContLayout = QVBoxLayout()
            taskName = data.get('task', 'Unknown')
            taskID = data.get('taskID')  # Get the taskID

            checkbox = QCheckBox(taskName)
            checkbox.setProperty("taskID", taskID)  # Set the taskID as a property of the checkbox

            taskCont.setLayout(taskContLayout)
            taskContLayout.addWidget(checkbox)

            # Add the new QFrame widget to the layout
            if existing_layout is None:
                existing_layout = QVBoxLayout()
                scrollWidget.setLayout(existing_layout)
            existing_layout.addWidget(taskCont)

            # Step 4: Connect checkbox state change signal to slot
            checkbox.toggled.connect(self.on_checkbox_toggled)

    def on_checkbox_toggled(self):
        """Slot to handle checkbox state changes"""
        sender = self.sender()  # Get the checkbox that triggered the signal

        # Get the taskID from the checkbox's property
        taskID = sender.property("taskID")

        if sender.isChecked():
            print(f"Task with ID {taskID} is checked!")
            self.updateJSONFile(self.tasksDir, taskID, 'complete')
            # reload table
            self.loadTasksTable()
        else:
            print(f"Task with ID {taskID} is unchecked!")
            self.updateJSONFile(self.tasksDir, taskID, 'incomplete')
    
    def updateJSONFile(self, file_path, task_id, new_status):
        """Update the task status in the JSON file based on taskID."""
        # Step 1: Read the existing data from the JSON file
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("The file was not found.")
            return
        except json.JSONDecodeError:
            print("Error reading the JSON file.")
            return

        # Step 2: Modify the data
        # Find the task by taskID and update its status
        for task in data:
            if task.get('taskID') == task_id:
                print(f"Updating task with ID {task_id}...")
                task['taskStatus'] = new_status  # Update the task status
                break
        else:
            print(f"Task with ID {task_id} not found.")
            return

        # Step 3: Write the updated data back to the JSON file
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  # Pretty print with 4 spaces for readability
            print(f"Task with ID {task_id} updated successfully.")
        except Exception as e:
            print(f"Error writing to the JSON file: {e}")

    def getData(self):
        """get all the data from the json file"""
        with open(self.tasksDir, 'r') as f:
            TaskData = json.load(f)
        return list(TaskData)

    def buttonConnections(self):
        """handles all the button connnections"""
        self.add_pushButton.clicked.connect(lambda: self.addBtnClicked())

    def addBtnClicked(self):
        """handles click event for add button"""
        # get input text
        input_text = self.new_item_lineEdit.text().strip()

        # check if input text is not empty
        if input_text != '':
            try:
                with open(self.tasksDir, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            newData = {
                "taskID": f"{self.generateTaskID()}{len(data) + 1}",
                "task": input_text,
                "taskStatus": 'incomplete'
            }

            data.append(newData)

            # insert input text into the .json file
            with open(self.tasksDir, 'w') as file:
                json.dump(data, file, indent=4)

            # clear the input field
            self.clearInput()
            # reload tasks list
            self.loadTasksTable()

    def generateTaskID(self):
        """generate task id"""
        randomNum = random.randint(0, 99)
        return f'TASK{randomNum}'

    def clearInput(self):
        """clears the input field"""
        self.new_item_lineEdit.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()  # Ensure the window is shown
    app.exec()