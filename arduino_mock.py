#A mock arduino to generate the data 
import requests
import json
from datetime import datetime 
import random 
import time 

def generate_mock_data():
    #Simulate dynamic sensor data 
    value=random.uniform(20.0,30.0) #Random temperature between 20 and 30 
    
    #static and dynamic data combined 
    data={
        "timestamp":datetime.now().isoformat(), #dynamic
        "sensor_id":"sensor_01", #Static
        "sensor_type":"temperature", #Static
        "value":value, #Dynamic
        "unit":"Celsius", #Static
        "location":"Building A, Melbourne", #Static
        "status":"OK", #Static
        "battery_level":95, #Static
        "calibration_date":"2024-05-01T00:00:00Z", #Static
        "environment_context":{"humidity":45,"pressure":1012}, #Static
        "data_quality":"Good" #Static

        
        }
    return data

def send_mock_data():
    url='http://127.0.0.1:8000/sensor/submit_data/' #replace with your actual endpoint URL
    
    while True:
        try:
            #Generate mock data 
            data=generate_mock_data()
            
            #Send the data to the django server
            response=requests.post(url,json=data)
            print(f"Status: {response.status_code}, Response:{response.text}")
            
            #Wait for a second before sending the next data point
            time.sleep(1)
            
        except Exception as e:
            print(f"Error: {e}")
            break
        
if __name__=="__main__":
    send_mock_data()