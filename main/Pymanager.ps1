$pythonVersion = $null
try {
    $pythonVersion = python --version
} catch {}

if ($null -eq $pythonVersion) {
    Write-Host "Python not found. Downloading Python installer..."
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe" -OutFile "python-3.9.7.exe"
    Write-Host "Installing Python..."
    Start-Process -FilePath ".\python-3.9.7.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
}

$pipVersion = $null
try {
    $pipVersion = pip --version
} catch {}

if ($null -eq $pipVersion) {
    Write-Host "pip not found. Downloading get-pip.py..."
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
    Write-Host "Installing pip..."
    python get-pip.py
}

python setup.py