#A mock arduino to generate the data 
import requests
import json
from datetime import datetime 
import random 
import time 

def generate_mock_data():
    #Simulate dynamic sensor data 
    #value=round(random.uniform(10.0,100.0)) #Random temperature between 20 and 30 
    #current_date=datetime.now().strftime("%Y-%m-%d")
    #sensor_types=['Temperature,Humidity','Pressure']
    sensor_data=[
    {'sensor_type':'Temperature','units':'°C','min_value':15.0,'max_value':35.0},
    {'sensor_type':'Humidity','units':'%','min_value':30.0,'max_value':70.0},
    {'sensor_type':'Pressure','units':'Pa','min_value':90000,'max_value':110000},
]
    
    random.shuffle(sensor_data)  # Shuffle the sensor data list
    
    for _ in range(3):  # Adjust the number of mock entries per second 
        for entry in sensor_data:
            sensor_type = entry['sensor_type']
            units = entry['units']
            min_value = entry['min_value']
            max_value = entry['max_value']
            current_date = datetime.now().strftime('%Y-%m-%d')
            
            value = round(random.uniform(min_value, max_value), 2)
    #static and dynamic data combined 
    data={
        "timestamp":datetime.now().isoformat(), #dynamic
        "sensor_id":"sensor_01", #Static
        "sensor_type": sensor_type, #dynamic
        "value":value, #Dynamic
        "unit":units, #Dynamic
        "location":"Building A, Melbourne", #Static
        "status":"OK", #Static
        "battery_level":95, #Static
        "calibration_date":current_date, #Dynamic 
        "environment_context":{"humidity":45,"pressure":1012}, #Static
        "data_quality":"Good" #Static

        
        }
    return data

def send_mock_data():
    url='http://127.0.0.1:8000/sensor/submit_data' #replace with your actual endpoint URL
    
    while True:
        try:
            #Generate mock data 
            data=generate_mock_data()
            
            #Send the data to the django server
            response=requests.post(url,json=data)
            print(f"Status: {response.status_code}, Response:{response.text}")
            
            #Wait for a second before sending the next data point
            time.sleep(15)
            
        except Exception as e:
            print(f"Error: {e}")
            break
        
if __name__=="__main__":
    send_mock_data()