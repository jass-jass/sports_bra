import requests
import matplotlib.pyplot as plt
import time

# Fetch the data from the server
url = "http://<server_ip>:5000/data-history"  # Replace <server_ip> with your Flask server's IP.
response = requests.get(url)
data = response.json()

# Separate data for plotting
timestamps = [entry['timestamp'] for entry in data]
accel_x = [entry['accel_x'] for entry in data]
accel_y = [entry['accel_y'] for entry in data]
accel_z = [entry['accel_z'] for entry in data]
gyro_x = [entry['gyro_x'] for entry in data]
gyro_y = [entry['gyro_y'] for entry in data]
gyro_z = [entry['gyro_z'] for entry in data]
emg = [entry['emg'] for entry in data]

# Plot accelerometer data
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(timestamps, accel_x, label='Accel X')
plt.plot(timestamps, accel_y, label='Accel Y')
plt.plot(timestamps, accel_z, label='Accel Z')
plt.legend()
plt.title("Accelerometer Data")
plt.xlabel("Time")
plt.ylabel("Acceleration (m/s^2)")

# Plot gyroscope data
plt.subplot(3, 1, 2)
plt.plot(timestamps, gyro_x, label='Gyro X')
plt.plot(timestamps, gyro_y, label='Gyro Y')
plt.plot(timestamps, gyro_z, label='Gyro Z')
plt.legend()
plt.title("Gyroscope Data")
plt.xlabel("Time")
plt.ylabel("Angular Velocity (°/s)")

# Plot EMG data
plt.subplot(3, 1, 3)
plt.plot(timestamps, emg, label='EMG', color='purple')
plt.legend()
plt.title("EMG Data")
plt.xlabel("Time")
plt.ylabel("Signal Strength")

plt.tight_layout()
plt.show()