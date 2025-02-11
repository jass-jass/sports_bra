#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <WiFi.h>
#include <HTTPClient.h>


Adafruit_MPU6050 mpu;

#define I2C_SDA 8
#define I2C_SCL 9

int emgPin = 2;
int emgValue = 0;
const char* ssid = "Hotspot";
const char* password = "876654321";
const char* serverURL = "http://192.168.115.88:5000/post-data";



void setup()
{
    Wire.begin(I2C_SDA, I2C_SCL);
    if(!mpu.begin())
    {
        while (1);
    }
    mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
    mpu.setGyroRange(MPU6050_RANGE_500_DEG);
    mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
    }
}



void loop()
{
    //////EMG
        emgValue = analogRead(emgPin);
    //MPU6050
        sensors_event_t accel, gyro, temp;
        mpu.getEvent(&accel, &gyro, &temp);
    /////WiFi
        if(WiFi.status()==WL_CONNECTED)
        {
            HTTPClient http;
            http.begin(serverURL);
            http.addHeader("Content-Type", "application/json");
            String payload = "{";
            payload += "\"accel\": {\"x\": " + String(accel.acceleration.x) + ", \"y\": " + String(accel.acceleration.y) + ", \"z\": " + String(accel.acceleration.z) + "},";
            payload += "\"gyro\": {\"x\": " + String(gyro.gyro.x) + ", \"y\": " + String(gyro.gyro.y) + ", \"z\": " + String(gyro.gyro.z) + "},";
            payload += "\"emg\": " + String(emgValue);
            payload += "}";

            int httpResponseCode = http.POST(payload);
            http.end();
        }
        delay(1000);
}
