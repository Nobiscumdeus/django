#include <SPI.h>
#include <Ethernet.h>
#include <HttpClient.h>

//Update the server IP to your Django server IP or domain 
char server[]="127.168.1.100"; //Replace with your django server IP

EthernetClient client;
HttpClient http(client,server,80);

//Replace with your Ethernet shield MAC address
byte mac[]={0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};

void setup(){
    Serial.begin(9600);

    //Initialize the Ethernet shield using DHCP

    if(Ethernet.begin(mac)==0){
        Serial.printIn("Failed to configure Ethernet using DHCP");
        for(;;);
    }
    delay(1000) ; //Give the Ethernet shield a second to initialize
}

void loop(){
    //Example sensor data
    String postData="{\"timestamp\":\"2024-05-21T15:30:00z\,\"sensor_id":\"sensor_01\",\"sensor_type\":\"temperature\",\"value\"23.5,\"unit\":\Celsius\",\"location\":\"Building A,Room 101\",\"status\":\"OK\",\"battery_level\":95,\"calibration_date\":\"2024-05-01T00:00:00Z\",\"environment_context\":{\"humidity\":45,\"pressure\":1012},\"data_quality\":\"Good\";

    //Make a HTTP Post Request
    http.beginRequest();
    http.post("/sensor/submit_data/");
    http.sendHeader("Content-Type","application/json");
    http.sendHeader("Content-Length",postData.length());
    http.beginBody();
    http.print(postData);
    http.endRequest();

    //Get the response status code and body
    int statusCode=http.responseStatusCode();
    String response=http.responseBody();
    Serial.print("Status: ");
    Serial.printIn(statusCode);
    Serial.print("Response: ");
    Serial.printIn(response);

    delay(60000); Wait for a minute  before sending the next data
    }
}
