import base64
import shutil
import os

file_name = "PYAuto"
icon = "assets\\lock-bot.ico"

with open(f"{file_name}.py", "r") as file:
    code = file.read()

# encoded_text = base64.b64encode(code.encode())
# with open(f"{file_name}.py", "w") as file:
    # file.write(f"import base64; exec(base64.b64decode({encoded_text}))")
    
os.system(f"pyinstaller --onefile --icon={icon} {file_name}.py")
shutil.rmtree("build")
os.remove(f"{file_name}.spec")

os.system("pause")
