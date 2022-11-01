import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

# Provide your IBM Watson Device Credentials
organization = "u7bs6g"
deviceType = "GasSensor"
deviceId = "121"
authMethod = "token"
authToken = "987654321"

try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
    deviceCli.connect()
# ..............................................

except ibmiotf.ConnectionException as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

while True:

    temp = random.randint(0, 100)
    hum = random.randint(0, 100)
    gas = random.randint(0, 100)

    mydata = {'temp': temp, 'hum': hum, 'gas': gas}

    def on_publish():
        print("Published Temperature = %s C" % temp, "Humidity = %s %%" % hum, "Gas Concentration = %s" % gas, "to IBM Watson")


    success = deviceCli.publishEvent("IOTGasSensor", "json", mydata, qos=0, on_publish=on_publish)
    if not success:
        print("Not connected to IoTF")
    time.sleep(2)

# Disconnect the device and application from the cloud
deviceCli.disconnect()
