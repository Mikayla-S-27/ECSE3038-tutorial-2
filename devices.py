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
    max_temp = 0
    for device in devices:
        if device["temp"] > max_temp:
            max_temp = device["temp"]
    for device in devices:
        if device["temp"] == max_temp:
            print(device)

hottest(readings)


def to_status(devices):
    for device in devices:
        if device["name"] == "fridge":
            name = device["name"]
            if device["online"] == True:
                status = "ok"
            else: status = "offline"
            celcius = device["temp"]
    new_object = {
        "device" : name,
        "status" : status,
        "celcius" : celcius
    }
    print(new_object)

to_status(readings)
        
