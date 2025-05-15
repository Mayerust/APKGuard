import os
import numpy as np

def create_permission_row(permission_file, master_permissions):
    """
    Create a binary row indicating the presence (1) or absence (0) of permissions.
    """
    with open(permission_file, "r") as f:
        apk_permissions = f.read().splitlines()

    # Creates binary row
    row = [1 if perm in apk_permissions else 0 for perm in master_permissions]
    return row

if __name__ == "__main__":
    # We defined 10 master permissions commonly used by malicious APKs
    master_permissions = [
        "android.permission.INTERNET",  # Network access
        "android.permission.READ_SMS",  # Access to SMS
        "android.permission.WRITE_EXTERNAL_STORAGE",  # Write to storage
        "android.permission.ACCESS_FINE_LOCATION",  # Location access
        "android.permission.RECORD_AUDIO",  # Record audio
        "android.permission.CAMERA",  # Camera access
        "android.permission.READ_CONTACTS",  # Access to contacts
        "android.permission.SEND_SMS",  # Send SMS
        "android.permission.RECEIVE_BOOT_COMPLETED",  # Auto-start after boot
        "android.permission.READ_CALL_LOG"  # Access call logs
    ]

    permission_dir = "/home/manas/Downloads/Permissions"  # Directory containing permission files
    matrix = []

    for permission_file in os.listdir(permission_dir):
        if permission_file.endswith(".txt"):
            permission_file_path = os.path.join(permission_dir, permission_file)
            row = create_permission_row(permission_file_path, master_permissions)
            matrix.append(row)

    # Converts to NumPy array and save
    matrix = np.array(matrix)
    np.save("permission_matrix.npy", matrix)
    print("Permission matrix generated and saved to permission_matrix.npy")
