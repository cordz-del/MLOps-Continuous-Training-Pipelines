# retrain_scheduler.py
import schedule
import time
from train_model import fine_tune_model  # assume this function retrains your model

def check_and_retrain():
    # Dummy condition: In production, compare evaluation metrics or check new data availability.
    should_retrain = True  # Replace with actual logic
    if should_retrain:
        print("Retraining model due to performance drop or new data...")
        fine_tune_model()
        print("Model retraining completed.")

# Schedule to check every hour
schedule.every(1).hours.do(check_and_retrain)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
