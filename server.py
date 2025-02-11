'''
from flask import Flask, request

app = Flask(__name__)

# List to store received data
data_history = []

@app.route('/post-data', methods=['POST'])
def receive_data():
    global data_history
    # Retrieve and store the received data
    received_data = request.data.decode('utf-8')
    data_history.append(received_data)
    print(f"Received data: {received_data}")
    
    # Respond to the ESP32-C3
    return f"Server received: {received_data}", 200

@app.route('/view-data', methods=['GET'])
def view_data():
    # Display all received data as an HTML page
    if data_history:
        html_response = "<h1>Data History</h1><ul>"
        for data in data_history:
            html_response += f"<li>{data}</li>"
        html_response += "</ul>"
        return html_response
    else:
        return "<h1>No data received yet.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''
'''
from flask import Flask, request, jsonify, render_template
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

app = Flask(__name__)

# Lists to store accelerometer and gyroscope data
accel_data = {'x': [], 'y': [], 'z': []}
gyro_data = {'x': [], 'y': [], 'z': []}

@app.route('/post-data', methods=['POST'])
def receive_data():
    global accel_data, gyro_data
    # Decode JSON payload
    received_data = request.get_json()
    if received_data:
        # Extract and store accelerometer data
        accel_data['x'].append(received_data['accel']['x'])
        accel_data['y'].append(received_data['accel']['y'])
        accel_data['z'].append(received_data['accel']['z'])
        # Extract and store gyroscope data
        gyro_data['x'].append(received_data['gyro']['x'])
        gyro_data['y'].append(received_data['gyro']['y'])
        gyro_data['z'].append(received_data['gyro']['z'])

        print(f"Received data: {received_data}")
        return "Data received and stored", 200
    else:
        return "Invalid JSON", 400

@app.route('/plot-accel', methods=['GET'])
def plot_accel():
    if not accel_data['x']:
        return "<h1>No accelerometer data to plot yet.</h1>"

    # Plot accelerometer data
    plt.figure(figsize=(8, 4))
    plt.plot(accel_data['x'], label='Accel X', marker='o')
    plt.plot(accel_data['y'], label='Accel Y', marker='o')
    plt.plot(accel_data['z'], label='Accel Z', marker='o')
    plt.xlabel('Data Points')
    plt.ylabel('Acceleration')
    plt.title('Accelerometer Data')
    plt.legend()

    # Save and encode plot as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f'<h1>Accelerometer Data</h1><img src="data:image/png;base64,{image_base64}"/>'

@app.route('/plot-gyro', methods=['GET'])
def plot_gyro():
    if not gyro_data['x']:
        return "<h1>No gyroscope data to plot yet.</h1>"

    # Plot gyroscope data
    plt.figure(figsize=(8, 4))
    plt.plot(gyro_data['x'], label='Gyro X', marker='o')
    plt.plot(gyro_data['y'], label='Gyro Y', marker='o')
    plt.plot(gyro_data['z'], label='Gyro Z', marker='o')
    plt.xlabel('Data Points')
    plt.ylabel('Gyroscope')
    plt.title('Gyroscope Data')
    plt.legend()

    # Save and encode plot as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f'<h1>Gyroscope Data</h1><img src="data:image/png;base64,{image_base64}"/>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''


from flask import Flask, request, jsonify, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Lists to store accelerometer, gyroscope, and EMG data
accel_data = {'x': [], 'y': [], 'z': []}
gyro_data = {'x': [], 'y': [], 'z': []}
emg_data = []  # For storing EMG values

@app.route('/post-data', methods=['POST'])
def receive_data():
    global accel_data, gyro_data, emg_data
    # Decode JSON payload
    received_data = request.get_json()
    if received_data:
        # Extract and store accelerometer data
        accel_data['x'].append(received_data['accel']['x'])
        accel_data['y'].append(received_data['accel']['y'])
        accel_data['z'].append(received_data['accel']['z'])
        # Extract and store gyroscope data
        gyro_data['x'].append(received_data['gyro']['x'])
        gyro_data['y'].append(received_data['gyro']['y'])
        gyro_data['z'].append(received_data['gyro']['z'])
        # Extract and store EMG data
        emg_data.append(received_data['emg'])

        print(f"Received data: {received_data}")
        return "Data received and stored", 200
    else:
        return "Invalid JSON", 400

@app.route('/plot-accel', methods=['GET'])
def plot_accel():
    if not accel_data['x']:
        return "<h1>No accelerometer data to plot yet.</h1>"

    # Plot accelerometer data
    plt.figure(figsize=(8, 4))
    plt.plot(accel_data['x'], label='Accel X', marker='o')
    plt.plot(accel_data['y'], label='Accel Y', marker='o')
    plt.plot(accel_data['z'], label='Accel Z', marker='o')
    plt.xlabel('Data Points')
    plt.ylabel('Acceleration')
    plt.title('Accelerometer Data')
    plt.legend()

    # Save and encode plot as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f'<h1>Accelerometer Data</h1><img src="data:image/png;base64,{image_base64}"/>'

@app.route('/plot-gyro', methods=['GET'])
def plot_gyro():
    if not gyro_data['x']:
        return "<h1>No gyroscope data to plot yet.</h1>"

    # Plot gyroscope data
    plt.figure(figsize=(8, 4))
    plt.plot(gyro_data['x'], label='Gyro X', marker='o')
    plt.plot(gyro_data['y'], label='Gyro Y', marker='o')
    plt.plot(gyro_data['z'], label='Gyro Z', marker='o')
    plt.xlabel('Data Points')
    plt.ylabel('Gyroscope')
    plt.title('Gyroscope Data')
    plt.legend()

    # Save and encode plot as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f'<h1>Gyroscope Data</h1><img src="data:image/png;base64,{image_base64}"/>'

@app.route('/plot-emg', methods=['GET'])
def plot_emg():
    if not emg_data:
        return "<h1>No EMG data to plot yet.</h1>"

    # Plot EMG data
    plt.figure(figsize=(8, 4))
    plt.plot(emg_data, label='EMG', marker='o', color='purple')
    plt.xlabel('Data Points')
    plt.ylabel('EMG Signal')
    plt.title('EMG Data')
    plt.legend()

    # Save and encode plot as an image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return f'<h1>EMG Data</h1><img src="data:image/png;base64,{image_base64}"/>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
