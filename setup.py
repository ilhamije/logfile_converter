# check if click is installed
import os

package = "click"

try:
    __import__package
except:
    os.system("pip install "+ package)