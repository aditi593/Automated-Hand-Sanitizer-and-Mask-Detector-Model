import random, string, os, requests
from main import run_server
from impl.utilities import backend_url, delete_device
import sys, os

file_name = os.getcwd() + '/manifests/.system.manifest'
activate_manifest = os.getcwd() + '/manifests/.activate'

def generate_deviceId():
    return 'AHS{0:07d}'.format(random.randint(0, 9999999))

def generate_api_key():
    return ''.join((random.choice(string.ascii_letters + '1234567890')) for x in range(20))  

def create_psf(id, api_key):
    manifest = "DEVICE_ID={DEVICE_ID}\nAPI_KEY={API_KEY}"
    try:
        with open(file_name, "w") as f:
            f.write(manifest.format(DEVICE_ID = id, API_KEY = api_key))
        return 1
    except Exception as e:
        print("Error Occured! ", e)
        return 0

def check_psf():
    try:
        f = open(file_name, "r")
        f.close()
        return 1
    except Exception as e:
        print("Registering Device.....")
        success = False
        while success != True:
            data = {
                'device_id' : generate_deviceId(),
                'api_key' : generate_api_key()
            }
            # Registering new devices to the database
            try:
                r = requests.post(backend_url+'device', json = data)
                res = r.json()
                if res['status'] == True:
                    create_psf(data['device_id'], data["api_key"])
                    print("To reset this device, use '-reset' argument with same command.\n\n\n\n")
                    success = True
                else:
                    continue
            except Exception as e:
                print('Error From Register Device: ', e)
                return 0
            # continue for next iteration
        return 1
        
def test_func():
    return 1

if __name__ == "__main__":
    if '-reset' in sys.argv:
        if os.path.exists(file_name):
            if delete_device():
                os.remove(file_name)
                os.remove(activate_manifest)
                print("Credentials deleted, start again to register.")
            else:
                print("Error Occured!")
        else:
            print("Credentials not found.")
        exit(1)
    if check_psf() == 1:
        run_server()
    else:
        print("Error reading manifests!")