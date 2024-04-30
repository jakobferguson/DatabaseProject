import subprocess
import sys

def check_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed.")
        install = input(f"Do you want to install {package}? (yes/no): ").strip().lower()
        if install == 'yes':
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        else:
            print(f"{package} installation skipped.")

# Check for Tkinter
try:
    import tkinter
except ImportError:
    print("Tkinter is not installed. Please ensure you have Tkinter enabled in your Python installation.")

# Check for Matplotlib
check_install('matplotlib')