import os
import shutil

folder_path = input("Enter folder path to organize: ").strip()

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}

# Create folders
for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    moved = True
                    break
            if moved:
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("Files organized successfully!")