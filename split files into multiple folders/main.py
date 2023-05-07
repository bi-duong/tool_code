import os
import shutil

folder_path = "D:/Py/IVCaption/video"
files = os.listdir(folder_path)
i = 0
folder_num = 1
for file in files:
    if i == 0:
        subfolder_path = os.path.join(folder_path, f"SubFolder{folder_num}")
        os.mkdir(subfolder_path)
    file_path = os.path.join(folder_path, file)
    subfolder_file_path = os.path.join(subfolder_path, file)
    shutil.move(file_path, subfolder_file_path)
    i += 1
    if i == 100:
        i = 0
        folder_num += 1
