import serial
import subprocess
import time

SERIAL_PORT = 'COM3'
SPEAKERS_DEVICE_NAME = 'Speakers'
HEADPHONE = 'Realtek HD Audio 2nd output'
NIRCMD_PATH = 'nircmd.exe'
NIRCMD_COMMAND_TEMPLATE = f'{NIRCMD_PATH} setdefaultsounddevice "{{device_name}}" 1'
FSR_THRESHOLD = 17000
SWITCH_INTERVAL = 2

def set_default_audio_output(device_name):
    """Sets the default audio output."""
    command = NIRCMD_COMMAND_TEMPLATE.format(device_name=device_name)
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f'Output from nircmd: {output}')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Failed to execute nircmd. Command: {command}, Error: {str(e)}')
        return False

def main():
    """Main function to run the script."""
    # Create a Serial object
    ser = serial.Serial(SERIAL_PORT, 9600)

    # Initialize timer
    last_switch_time = time.time()

    # Set initial output device
    current_device = HEADPHONE

    while True:
        if ser.inWaiting() > 0:  # if data is available to read
            try:
                data = ser.readline().decode('utf-8').strip()  # read a line, decode to string and strip newline
                print(data)
                if 'FSR Reading : ' in data:  # Check if data contains FSR reading
                    fsr_reading = int(data.split(':')[1])  # Extract the FSR reading from data
                    current_time = time.time()
                    if (fsr_reading > FSR_THRESHOLD and current_time - last_switch_time >= SWITCH_INTERVAL
                            and current_device != SPEAKERS_DEVICE_NAME):
                        current_device = SPEAKERS_DEVICE_NAME
                        if switch_audio_output_device(current_device, current_time):
                            last_switch_time = current_time
                    elif (fsr_reading <= FSR_THRESHOLD and current_time - last_switch_time >= SWITCH_INTERVAL
                          and current_device != HEADPHONE):
                        current_device = HEADPHONE
                        if switch_audio_output_device(current_device, current_time):
                            last_switch_time = current_time
            except Exception as e:
                print(f'Error decoding data: {e}')

def switch_audio_output_device(device_name, current_time):
    """Switches the audio output device and returns success status."""
    success = set_default_audio_output(device_name)
    if success:
        print(f'Successfully set {device_name} as the default audio output.')
    else:
        print(f'Failed to set {device_name} as the default audio output.')
    return success

if __name__ == '__main__':
    main()

