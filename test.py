import math
import sys
from os import rename

import requests


def greet(who):
    test = "Test"
    greeting = "Hello, {}".format(who)
    return greeting


# print(sys.version)
# print(sys.executable)
r = requests.get("https://coreyms.com")
print(r.status_code)
