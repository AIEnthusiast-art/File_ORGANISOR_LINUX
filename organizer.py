import os
import shutil

# 📁 Define categories and their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

def organize_files(target_folder):
    if not os.path.exists(target_folder):
        print(f"❌ Folder not found: {target_folder}")
        return

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_path = os.path.join(target_folder, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"✅ Moved: {filename} → {category}/")
                    break

if __name__ == "__main__":
    folder_to_organize = input("Enter the path to the folder you want to organize: ")
    organize_files(folder_to_organize)
