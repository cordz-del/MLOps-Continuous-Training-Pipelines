# retrain_trigger.py
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from train_model import fine_tune_model

class DataUpdateHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("new_data.csv"):
            print("New data detected. Triggering model retraining...")
            fine_tune_model()
            print("Retraining completed.")

if __name__ == "__main__":
    path = "./data/"
    event_handler = DataUpdateHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("Monitoring data directory for changes...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
