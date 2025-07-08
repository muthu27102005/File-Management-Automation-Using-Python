import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# List of Files that we can convert
file_types = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"],
    "Code": [".py", ".html", ".css", ".js", ".ts", ".java", ".cpp", ".json", ".xml"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk"]
}

# Function to organize files by copying
def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)

                    # Copy instead of move
                    try:
                        shutil.copy(file_path, os.path.join(dest_folder, file))
                    except Exception as e:
                        print(f"Error copying {file}: {e}")

    messagebox.showinfo("Success", "Files copied and organized successfully!")

#  Folder selector
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

#  GUI setup
app = tk.Tk()
app.title("Smart File Organizer (Safe Copy Version)")
app.geometry("400x200")

label = tk.Label(app, text="📁 Click below to organize your files (by Copy)", font=("Arial", 11))
label.pack(pady=15)

button = tk.Button(app, text="Select Folder", font=("Arial", 12), command=select_folder)
button.pack(pady=10)

footer = tk.Label(app, text="Created by Muthu ", font=("Arial", 9), fg="gray")
footer.pack(side="bottom", pady=10)

app.mainloop()
