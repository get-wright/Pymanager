If you have problems in installing dependencies, you could try to install by yourself:

- **For Python:** https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
 
- **For pip:**
Download `get-pip.py` from https://bootstrap.pypa.io/get-pip.py. Then, open a command prompt window and navigate to the location where you saved 'get-pip.py'. Run the following command:
```
python get-pip.py
```
This will install pip globally. If you want to install it for a specific Python version, replace python with the version you want:
```
python3 get-pip.py
```

- **For `pandas`, `apyori`, `flask`, `Werkzeug`:**
You can install all of them by typing into the 'Command Prompt'
```
pip install pandas apyori flask Werkzeug
```