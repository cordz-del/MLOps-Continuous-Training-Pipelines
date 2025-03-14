# evaluation_metrics.py
from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(true_labels, predictions):
    accuracy = accuracy_score(true_labels, predictions)
    f1 = f1_score(true_labels, predictions, average="weighted")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weighted F1 Score: {f1:.4f}")
    return accuracy, f1

# Example usage
if __name__ == "__main__":
    true_labels = [0, 1, 1, 0, 1]
    predictions = [0, 1, 0, 0, 1]
    evaluate_model(true_labels, predictions)
