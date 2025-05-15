from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def train_and_evaluate(matrix, labels):
    """
    Train and evaluate a Random Forest model.
    """
    # Splits dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(matrix, labels, test_size=0.2, random_state=42)

    # Train Random Forest Classifier model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    return model

if __name__ == "__main__":
    # Loads the permission matrix
    permission_matrix = np.load("permission_matrix.npy")

    # Defines labels for the APKs (1 = malicious, 0 = benign)
    labels = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]  # Example for 10 APKs

    # Trains and evaluate the model
    trained_model = train_and_evaluate(permission_matrix, labels)

    # Saves the trained model
    import joblib
    joblib.dump(trained_model, "trained_model.pkl")
    print("Trained model saved as trained_model.pkl")