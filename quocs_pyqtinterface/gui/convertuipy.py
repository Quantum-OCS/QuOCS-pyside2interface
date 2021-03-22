import os

ui_folder = os.path.join(os.getcwd(), "uifiles")
class_folder = os.path.join(os.getcwd(), "uiclasses")
for file in os.scandir(ui_folder):
    if file.path.endswith(".ui"):
        class_file = os.path.splitext(file)[0] + "UI.py"
        os.system("python -m PyQt5.uic.pyuic -x {0} -o {1}".format(file.path, class_file))
        os.system("mv {0} {1}".format(class_file, class_folder))
