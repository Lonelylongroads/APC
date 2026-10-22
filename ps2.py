import os
import shutil

folder_path = "my_folder"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        ext = filename.split('.')[-1] if '.' in filename else 'others'
        dest_folder = os.path.join(folder_path, ext)
        
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, filename))