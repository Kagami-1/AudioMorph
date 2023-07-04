import subprocess

def list_audio_devices():
    command = 'nircmd.exe showsounddevices'
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output.strip().split('\n')
    except subprocess.CalledProcessError:
        return None

# Example usage
devices = list_audio_devices()
if devices:
    print("Audio Devices:")
    for device in devices:
        print(device)
else:
    print("Failed to retrieve audio devices.")
