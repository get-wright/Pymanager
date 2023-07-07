@echo off
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found.
    set /p installPython="Do you want to install Python? (y/n): "
    if /i "%installPython%"=="y" (
        echo Downloading Python installer...
        powershell -Command "Invoke-WebRequest -OutFile python-3.9.7.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
        echo Installing Python...
        start /wait python-3.9.7.exe InstallAllUsers=1 PrependPath=1
        echo Python installation complete.
        cscript //nologo refreshenv.vbs
    )
)

where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip not found.
    set /p installPip="Do you want to install pip? (y/n): "
    if /i "%installPip%"=="y" (
        echo Downloading get-pip.py...
        powershell -Command "Invoke-WebRequest -OutFile get-pip.py https://bootstrap.pypa.io/get-pip.py"
        echo Installing pip...
        start /wait python get-pip.py
        echo pip installation complete.
        cscript //nologo refreshenv.vbs
    )
)

python setup.py
