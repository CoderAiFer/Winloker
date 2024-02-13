import os
import subprocess

path_to_py = "D:\Project\script.py" #укажите путь к вашему коду

if not os.path.exists(path_to_py):
    print("Файл не существует")
    exit()

path_to_exe = os.path.dirname(path_to_py) + "/exe"
os.makedirs(path_to_exe, exist_ok=True)

subprocess.call([
    "pyinstaller",
    "-F",
    "-w",
    "-n",
    os.path.basename(path_to_py).replace(".py", ""),
    path_to_py
])

print("Файл .py успешно преобразован в .exe")
