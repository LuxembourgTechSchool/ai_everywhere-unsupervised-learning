import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("matplotlib")
install("numpy")
install("opencv-python")
install("scikit-learn")
