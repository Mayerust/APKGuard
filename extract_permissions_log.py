from androguard.core.bytecodes.apk import APK
import os

def extract_permissions(apk_file):
    """
    Extract permissions from the AndroidManifest.xml file in an APK.
    """
    apk = APK(apk_file)
    return apk.get_permissions()

if __name__ == "__main__":
    apk_dir = os.path.expanduser("/home/manas/Downloads/APKs")  # Directory containing APK files
    output_dir = os.path.expanduser("/home/manas/Downloads/Permissions")  # Directory to save permission logs
    os.makedirs(output_dir, exist_ok=True)
 
    count = 0
    for apk_file in os.listdir(apk_dir):
        if apk_file.endswith(".apk"):
            if count >= 10:  # Limit to 10 APKs
                break
            apk_path = os.path.join(apk_dir, apk_file)
            output_file = os.path.join(output_dir, f"{os.path.splitext(apk_file)[0]}_permissions.txt")

            # Skip  the existing files
            if os.path.exists(output_file):
                print(f"Permissions file already exists for {apk_file}. Skipping.")
                continue

            try:
                permissions = extract_permissions(apk_path)
            except Exception as e:
                print(f"Error processing {apk_file}: {e}")
                continue

            # Saves permissions to a file
            with open(output_file, "w") as f:
                f.write(f"APK: {apk_file}\n")
                f.write("Permissions Extracted:\n")
                f.write("\n".join(permissions))

            print(f"Permissions extracted for {apk_file} and saved to {output_file}")
            count += 1