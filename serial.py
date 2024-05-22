import serial
import requests
import json
from datetime import datetime 

#Configure the serial port(adjust as necessary)
ser=serial.Serial('dev/ttyUSB0',9600) #For windows it might be COM3,COM4

while True:
    try:
        #Read a line of data from the serial port 
        line=ser.readline().decode('utf-8').strip()
        value=float(line)
        
        #create a dictionary to hold the data 
        data={
            "timestamp":datetime.now().isoformat(),
            "sensor_id":"sensor_01",
            "sensor_type":"temperature",
            "value":value,
            "unit":"Celsius",
            "location":"Building A,Room 101",
            "status":"OK",
            "battery_level":95,
            "calibration_date":"2024-05-01T00:00:00Z",
            "environment_context":{"humidity":45,"pressure":1012},
            "data_quality":"Good"
        }
        
        #Send the data to the Django server
        response=requests.post("http://127.0.0.1:8000/sensor/submit_data/",json=data)
        print(f"Status: {response.status_code}, Response:{response.text}")
        
    except Exception as e:
        print(f"Error: {e}")
        break
                                   