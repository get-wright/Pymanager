@echo off
python --version >nul 2>&1 || (
    echo Python not found.
    set /p installPython="Do you want to install Python? (y/n): "
    if /i "%installPython%"=="y" (
        echo Installing Python...
        msiexec /i python-3.x.x.msi /passive /norestart
    )
)
pip --version >nul 2>&1 || (
    echo pip not found.
    set /p installPip="Do you want to install pip? (y/n): "
    if /i "%installPip%"=="y" (
        echo Installing pip...
        python get-pip.py
    )
)
python setup.py