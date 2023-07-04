import serial
import subprocess
from time import sleep

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

while True:
    if ser.inWaiting() > 0:  # if data is available to read
        try:
            data = ser.readline().decode('utf-8').strip()  # read a line, decode to string and strip newline
            print(data)
            if "Analog reading = " in data:  # Check if data contains FSR reading
                fsr_reading = int(data.split("= ")[1])  # Extract the FSR reading from data
                if fsr_reading > 12000:
                    print('FSR Reading is above 1000')
                    device_name = 'Speakers'
                    #sleep(1.5)
                else:
                    device_name = 'Realtek HD Audio 2nd output'
                    #sleep(1.5)
                success = set_default_audio_output(device_name)
                if success:
                    print(f"Successfully set '{device_name}' as the default audio output.")
                else:
                    print(f"Failed to set '{device_name}' as the default audio output.")
        except Exception as e:
            print(f"Error decoding data: {e}")
