import serial, time

#Arduino Configuration
port = '/dev/cu.usbmodem14101'
arduino = serial.Serial(port, 9600, timeout=.1)
time.sleep(1) 

#Process which should be done if mask is detected
def found():
    data = "1"
    arduino.write(data.encode())
    time.sleep(4) # Meanwhile arduino will detect hand and will spray sanitizer
    incoming = arduino.readline()
    incoming = incoming.decode()
    if incoming == "not_done":
        return False
    else:
        return incoming