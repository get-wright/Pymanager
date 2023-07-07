import subprocess
import sys
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check for tqdm first
try:
    import tqdm
except ImportError:
    user_input = input("tqdm is not installed. Do you want to install it? (yes/no): ")
    if user_input.lower() == 'yes':
        print("Installing tqdm...")
        install('tqdm')
        print("tqdm installed successfully.")
        time.sleep(5)  # Pause for 5 seconds
    else:
        sys.exit("Installation cancelled by user.")

# Add other dependencies here
dependencies = ['os', 'pandas', 'apyori', 'flask', 'werkzeug']

for dependency in dependencies:
    try:
        __import__(dependency)
    except ImportError:
        user_input = input(f"{dependency} is not installed. Do you want to install it? (yes/no): ")
        if user_input.lower() == 'yes':
            print(f"Installing {dependency}...")
            install(dependency)
            print(f"{dependency} installed successfully.")
            time.sleep(5)  # Pause for 5 seconds
        else:
            sys.exit("Installation cancelled by user.")

import pymain

pymain.app.run(debug=False)

