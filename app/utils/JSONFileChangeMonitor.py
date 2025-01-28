import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JsonFileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def on_modified(self, event):
        if event.src_path == self.file_path:
            print(f"File {self.file_path} has been modified.")
            self.handle_file_change()

    def handle_file_change(self):
        # Load and print the updated JSON content
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                print("Updated JSON content:", data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")

# if __name__ == "__main__":
#     # Path to the JSON file to monitor
#     file_to_watch = "data.json"

#     # Create an event handler and observer
#     event_handler = JsonFileChangeHandler(file_to_watch)
#     observer = Observer()
#     observer.schedule(event_handler, path=".", recursive=False)

#     # Start the observer
#     observer.start()
#     print(f"Monitoring changes to {file_to_watch}...")
 
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Stopping monitoring...")
#         observer.stop()

#     observer.join()