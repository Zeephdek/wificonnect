import os
import re


def main():
    default_ahk_path = r'C:\Code\Startup\Currently Running.ahk'
    ahkcode = """;wificonn_start
<#+F3:: Run, pythonw.exe "FILEPATH", DIRECTORY
;wificonn_end
"""
    
    cdir = os.getcwd()

    current_ahk_text = open(default_ahk_path, "r").read()
    print("AHK file read successfully.")
    
    if ";wificonn_start" not in current_ahk_text or ";wificonn_end" not in current_ahk_text:
        current_ahk_text = current_ahk_text + "\n\n;wificonn_start\n\n;wificonn_end"

    current_ahk_text = current_ahk_text.replace("\\", "\\\\")

    dir_to_main = os.path.join(cdir, "main.pyw") # asuming main.pyw is the default file
    
    ahkcode = ahkcode.replace('FILEPATH', dir_to_main).replace('DIRECTORY', cdir).replace("\\", "\\\\")

    newfile = re.sub(
        r';wificonn_start(.*)|((\n)*);wificonn_end', 
        ahkcode,
        current_ahk_text,
        flags=re.DOTALL
        )

    newfile = newfile.replace("\\\\", "\\")


    # writing
    with open(default_ahk_path, "w") as f:
        f.write(newfile)

    input("Operation completed successfully. Press Enter to close.")

if __name__ == "__main__":
    main()
