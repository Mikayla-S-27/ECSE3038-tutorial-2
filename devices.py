readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True}
]

def list_devices(devices):
    for device in devices:
        print(device["name"] , device["temp"])

list_devices(readings)


def average_temp(devices):
    temp_sum = 0
    count = 0
    for device in devices:
        temp_sum += device["temp"]
        count += 1
    return temp_sum / count

print(average_temp(readings))


def hottest(devices):
    hot = devices[0]
    for device in devices:
        if device["temp"] > hot["temp"]:
            hot = device
    return hot

print (hottest(readings))


def to_status(device):
    if device["online"]:
        status = "ok"
    else:
        status = "offline"
    return {"device": device["name"], "status": status, "celsius": device["temp"]}

print(to_status(readings[3]))

def by_room(devices):
    rooms = {}
    for device in devices:
        room = device["room"]
        if room not in rooms:
            rooms[room] = []
        rooms[room].append(device["name"])
    return rooms
        
print (by_room(readings))

        
