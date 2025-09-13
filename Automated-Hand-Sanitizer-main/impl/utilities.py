import os, requests

manifest_path = os.getcwd() + '/manifests/.system.manifest'
artifacts_path = os.getcwd() + '/artifacts/'
backend_url = "http://sanitizer-backend.herokuapp.com/v1/"
#backend_url = 'http://127.0.0.1:5000/v1/'

def get_device_info():
    with open(manifest_path, "r") as f:
        manifest = f.readlines()
        device_id = manifest[0].split("=")[1][:-1]
        device_api = manifest[1].split("=")[1]
        return device_id, device_api
    
def update_quantity(qty):
    url = backend_url + 'device'
    data = {
        'sanitizer_qty':qty
    }
    device_id, api = get_device_info()
    header = {
        'x-device-id':device_id,
        'x-api-key': api
    }
    try:
        r = requests.patch(url, json=data, headers=header)
        res = r.json()
        if res['status'] == True:
            return 1
        else:
            return 0
    except Exception as e:
        print(e)
        return 0

def delete_device():
    url = backend_url + 'device'
    device_id, api = get_device_info()
    header = {
        'x-device-id':device_id,
        'x-api-key': api
    }
    try:
        r = requests.delete(url, headers=header)
        res = r.json()
        if res['status'] == True:
            return 1
        else:
            return 0
    except Exception as e:
        print(e)
        return 0

def check_device_status():
    url = backend_url + 'device/status'
    device_id, _ = get_device_info()
    try:
        param = {
            'device_id': device_id
        }
        r = requests.get(url, params=param)
        res = r.json()
        if res['status'] == True:
            return 1
        else:
            return 0
    except Exception as e:
        print('Error From Status Check: ', e)
