import time
import serial

ser = serial.Serial('COM3', 9600)

# add a variable to store the last time you switched outputs
last_switch_time = time.time()
# add a variable to store the current audio output device
current_device = None
# define a delay (in seconds) that needs to pass before switching again
delay = 2.0  # adjust this value as needed

while True:
    if ser.inWaiting() > 0:  # if data is available to read
        try:
            data = ser.readline().decode('utf-8').strip()  # read a line, decode to string and strip newline
            print(data)
            if "Analog reading = " in data:  # Check if data contains FSR reading
                fsr_reading = int(data.split("= ")[1])  # Extract the FSR reading from data
                if fsr_reading > 12000 and (current_device != 'Speakers' or time.time() - last_switch_time > delay):
                    print('FSR Reading is above 10000')
                    device_name = 'Speakers'
                elif current_device != 'Realtek HD Audio 2nd output' or time.time() - last_switch_time > delay:
                    device_name = 'Realtek HD Audio 2nd output'
                else:
                    continue  # if not enough time has passed, skip the rest of the loop

                success = set_default_audio_output(device_name)
                if success:
                    print(f"Successfully set '{device_name}' as the default audio output.")
                    # update the last switch time and current device
                    last_switch_time = time.time()
                    current_device = device_name
                else:
                    print(f"Failed to set '{device_name}' as the default audio output.")
        except Exception as e:
            print(f"Error decoding data: {e}")
