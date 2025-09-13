import cv2, os

from impl.mask_detection import detect, found

# Take Camera Input
camera = cv2.VideoCapture(0)

# Path to Haar Cascade
hc = os.getcwd() + '/artifacts/haarcascade_frontalface_default.xml'

# Msg to send at front end
msg = []
msg.append("")

def gen_frames():  
    while True:
        success, img = camera.read()  # read the camera frame
        if not success:
            break
        else:
            face_cascade = cv2.CascadeClassifier(hc) 
            img = cv2.flip( img, 1 )
            showImg = img
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            msg[0] = ""
            for (x,y,w,h) in faces:
                send = img[y:y+h, x:x+w]
                # Going for image processing
                # TODO: Python waiting for all sanitizer process and then returning frame.
                # TODO: Implement websockets to send data to front end
                msg[0] = detect(send)
                if msg[0] == "Mask Found":
                    msg[0] = found()
                # TODO: Implement proper status shown
            
            ret, buffer = cv2.imencode('.jpg', showImg)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result