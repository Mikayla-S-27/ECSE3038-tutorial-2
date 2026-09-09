readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True}
]

def list_devices(devices):
    for device in devices:
        print(device["name"] + " temp is: " + str(device["temp"]))

print(list_devices(readings))

def average_temp(devices):
    temp_sum = 0
    count = 0
    for device in devices:
        temp_sum += device["temp"]
        count += 1
    return temp_sum / count if count > 0 else 0

print(average_temp(readings))