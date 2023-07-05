import serial
import subprocess
from time import sleep, time

# Function to set default audio output
def set_default_audio_output(device_name):
    command = f'nircmd.exe setdefaultsounddevice "{device_name}" 1'
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Output from nircmd: {output}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute nircmd. Command: {command}, Error: {str(e)}")
        return False

# Create a Serial object
ser = serial.Serial('COM3', 9600)

# Initialize timer
last_switch_time = time()

# Set initial output device
current_device = 'Realtek HD Audio 2nd output'

while True:
    if ser.inWaiting() > 0:  # if data is available to read
        try:
            data = ser.readline().decode('utf-8').strip()  # read a line, decode to string and strip newline
            print(data)
            if "Analog reading = " in data:  # Check if data contains FSR reading
                fsr_reading = int(data.split("= ")[1])  # Extract the FSR reading from data
                current_time = time()
                if fsr_reading > 12000 and current_time - last_switch_time >= 2 and current_device != 'Speakers':
                    print('FSR Reading is above 15000')
                    current_device = 'Speakers'
                    success = set_default_audio_output(current_device)
                    if success:
                        print(f"Successfully set '{current_device}' as the default audio output.")
                        last_switch_time = current_time
                    else:
                        print(f"Failed to set '{current_device}' as the default audio output.")
                elif fsr_reading <= 12000 and current_time - last_switch_time >= 2 and current_device != 'Realtek HD Audio 2nd output':
                    current_device = 'Realtek HD Audio 2nd output'
                    success = set_default_audio_output(current_device)
                    if success:
                        print(f"Successfully set '{current_device}' as the default audio output.")
                        last_switch_time = current_time
                    else:
                        print(f"Failed to set '{current_device}' as the default audio output.")
        except Exception as e:
            print(f"Error decoding data: {e}")
