import json
import pyttsx3
import requests
import psutil

engine = pyttsx3.init()

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(2))

# Getting % usage of virtual_memory (3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])

# engine.runAndWait()
