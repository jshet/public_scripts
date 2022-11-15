import requests
from importlib import reload
from time import sleep
import json

import app_play.config as config
import app_play.my_id as my_id 

debug = True

def update():
    if debug == True:
        url = config.DEV_UPDATE_URL
        freq = config.DEV_UPDATE_FREQ        
    else:
        url = config.UPDATE_URL
        freq = config.UPDATE_FREQ
    
    import app_play.ota_updated_app as ota_updated_app
    try:
        print(f'{url=}, {freq=}')
        r = requests.get(url)
        with open('ota_updated_app.py', 'w') as f:
            f.write(r.text)
        
        ota_updated_app = reload(ota_updated_app)

    except Exception as ex:
        print(ex)
        exit()
    
    sleep(freq)

def setup():
    print("Welcome, let's get you setup.\nTurning on wifi...")
    new_id = input("Enter device ID:")
    with open("my_id.py", "w") as f:
        f.write(f"DEVICE_ID={new_id}")

while True:
    try:
        with open("my_id.json", "r") as f:
            j = json.loads(f.read())
            id = j["DEVICE_ID"]
            print(id)
    except:
        setup()
        
    try:
        update()
    except:
        exit()