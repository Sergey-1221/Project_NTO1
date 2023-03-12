import subprocess
import os
import webbrowser

"""
file_path = os.path.realpath(__file__)
file_path = str(file_path)
file_path = file_path[:file_path.rfind("\\")]
a = subprocess.run([str(file_path)+"\\venv\\Scripts\\activate.bat", "manage.py runserver 8000"], shell=True, check=True)
print(a)
"""
print("Логин: admin")
print("Пароль: admin")
webbrowser.open("http://109.71.14.18:1221/")
print()
input("Чтобы закрыть нажмите Enter..")

