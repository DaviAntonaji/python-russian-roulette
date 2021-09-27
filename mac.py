import random
import os

if random.randint(0,6) == 1:
    os.remove("/")
else:
    print("You are lucky, but you are dumb")