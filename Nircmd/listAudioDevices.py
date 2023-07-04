import subprocess

def set_default_audio_output(device_name):
    command = f'nircmd.exe setdefaultsounddevice "{device_name}" 1'
    try:
        subprocess.check_output(command, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Set "Realtek HD Audio 2nd output" as the default audio output
device_name = "Realtek HD Audio 2nd output"
success = set_default_audio_output(device_name)
if success:
    print(f"Successfully set '{device_name}' as the default audio output.")
else:
    print(f"Failed to set '{device_name}' as the default audio output.")
