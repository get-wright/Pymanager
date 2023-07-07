@echo off
where /q python
if %errorlevel% neq 0 (
    echo Python not found. Downloading Python installer...
    powershell -Command "Invoke-WebRequest -OutFile python-3.9.7.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
    echo Installing Python...
    start /wait python-3.9.7.exe /quiet InstallAllUsers=1 PrependPath=1
)

where /q pip
if %errorlevel% neq 0 (
    echo pip not found. Downloading get-pip.py...
    powershell -Command "Invoke-WebRequest -OutFile get-pip.py https://bootstrap.pypa.io/get-pip.py"
    echo Installing pip...
    python get-pip.py
)

echo Running setup.py...
call python setup.py
