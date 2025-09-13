# Imports
from flask import Flask, render_template, Response, jsonify

# Projects impl imports
from impl.opencv import gen_frames, msg
from impl.utilities import get_device_info, check_device_status
import os

# Initiating Flask
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static/', 
            static_folder='static/')

# Index Page
@app.route('/')
def index():
    try:
        activate_manifest = os.getcwd() + '/manifests/.activate'
        if os.path.exists(activate_manifest):
            return render_template('index.html')
        elif check_device_status() == 1:
            f = open(activate_manifest, "w")
            f.close()
            return render_template('index.html')
        else:
            device_id, api_key = get_device_info()
            return render_template('register_device.html', device = {'device_id':device_id, 'api_key':api_key})
    except Exception as e:
        print(e)

# For video streaming
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# This will be replaced with web sockets    
@app.route('/mask_status', methods = ['GET'])
def mask_status():
    return jsonify({'Mask_Status': msg[0]})

@app.route('/check-certificate', methods = ['GET'])
def check_certificate():
    return render_template('check-certificate.html')

def run_server():
    app.run(port=5001,debug=True)