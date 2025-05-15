import os
import numpy as np
import joblib
from androguard.core.bytecodes.apk import APK

def extract_permissions(apk_file):
    """
    Extract permissions from the AndroidManifest.xml file in an APK.
    """
    apk = APK(apk_file)
    return apk.get_permissions()

def create_permission_row(apk_permissions, master_permissions):
    """
    Create a binary row indicating the presence (1) or absence (0) of permissions.
    """
    row = [1 if perm in apk_permissions else 0 for perm in master_permissions]
    return row

if __name__ == "__main__":
    # Master list of permissions (used during training)
    master_permissions = [
        "android.permission.INTERNET",
        "android.permission.READ_SMS",
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.RECORD_AUDIO",
        "android.permission.CAMERA",
        "android.permission.READ_CONTACTS",
        "android.permission.SEND_SMS",
        "android.permission.RECEIVE_BOOT_COMPLETED",
        "android.permission.READ_CALL_LOG"
    ]

    # Directory containing new APKs to analyze
    apk_dir = ("/home/manas/Downloads/NEWAPK").strip()

    if not os.path.exists(apk_dir) or not os.path.isdir(apk_dir):
        print(f"Error: Directory '{apk_dir}' not found or is not a directory.")
        exit(1)

    # Loaded the trained model
    model_path = "trained_model.pkl"
    if not os.path.exists(model_path):
        print(f"Error: Trained model file '{model_path}' not found.")
        exit(1)
    model = joblib.load(model_path)

    # Initialized matrix and results
    permission_matrix = []
    results = []

    print("\nAnalyzing APKs...")
    for apk_file in os.listdir(apk_dir):
        if apk_file.endswith(".apk"):
            apk_path = os.path.join(apk_dir, apk_file)
            print(f"Processing {apk_file}...")

            try:
                # Step 1: Extract permissions
                apk_permissions = extract_permissions(apk_path)

                # Step 2: Create binary permission row
                test_row = create_permission_row(apk_permissions, master_permissions)
                permission_matrix.append(test_row)

                # Step 3: Predict
                prediction = model.predict([test_row])[0]
                results.append((apk_file, "Malicious" if prediction == 1 else "Benign"))
            except Exception as e:
                print(f"Error processing {apk_file}: {e}")
                continue

    # Converts matrix to NumPy array
    permission_matrix = np.array(permission_matrix)

    # Display the matrix and results
    print("\nPermission Matrix:")
    print(permission_matrix)
    print("\nClassification Results:")
    for apk, result in results:
        print(f"{apk}: {result}")