
**HackMD LINK: https://hackmd.io/@DXeFrrZgQFulz06N82SQHg/HJOFmHbtn**
**Shoeb Chowdhury / SC222RF**

A Smart Headphone Stand that switches audio output using FSR (Force Sensitive Resistor).


**Amount of time required to replicate the project:** ~2 hours

## Objective

![](https://hackmd.io/_uploads/r1WOs5NF3.jpg)

The goal of the "AudioMorph" project is to create a smarter sound system. Using a pressure-sensitive resistor (FSR) and a Raspberry Pi Pico WH, the aim was to automatically switch the computer's audio output between speakers and headphones based on whether the headphones are resting on the headphone stand or not. I found it very interesting and intuitive that many TWS (True Wireless Stereo) earphones were able to achieve this for smartphones, but there wasn't any such solution available for desktop users with headphones. So, my goal was to create something for myself.

---

## Materials Used

Component | Link | Bought at | Price* 
-| -| -| -
Raspberry Pi Pico WH |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/)| electrokit.com | 399 SEK**
Jumper wires         |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Breadboard          |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Micro USB cable      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Headphone Stand | [link](https://www.amazon.se/dp/B071S5JH2R?psc=1&ref=ppx_yo2ov_dt_b_product_details)|amazon.se | 99 SEK*
SD1306 0.9" OLED screen               |[link](https://www.amazon.se/dp/B01L9GC470?psc=1&ref=ppx_yo2ov_dt_b_product_details)| amazon.se | 76 SEK*
FSR (Pressure-Sensitive Resistor) 0.5"       |     [link](https://www.electrokit.com/produkt/tryckkansligt-motstand-0-5/)| electrokit.com | 79 SEK*
10k Resistor      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 1 SEK**
LEDs      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 10 SEK**


\* All prices are approximate.

\** Components were part of a kit, so they may be cheaper when bought individually.

---

![](https://hackmd.io/_uploads/rkE3zjVYn.jpg)

**Figure 1**: *Raspberry Pi Pico WH*. 

The microcontroller used in this project is responsible for reading data from the FSR and determining the necessary audio output switch based on the pressure detected.

![](https://hackmd.io/_uploads/rJRKMsVK3.jpg)

**Figure 2**: *SD1306 0.9" OLED screen*. 

This device is used to display the readings of the analog reading and other animations.

![](https://hackmd.io/_uploads/Byezzj4Y3.jpg)

**Figure 3**: *Jumper wires*. 

These wires are used to connect the Raspberry Pi Pico to the FSR and provide power.

![](https://hackmd.io/_uploads/HyIUGj4t2.jpg)

**Figure 4**: *Breadboard*. 

The breadboard serves as a base for connections and allows for easy assembly and disassembly of the system.

![](https://hackmd.io/_uploads/BkKXQoEK3.jpg)

**Figure 5**: *FSR402 Pressure-Sensitive Resistor 0.5"*. 

The FSR consists of a layer of polymer sandwiched between two conductive layers. This polymer layer decreases in resistance as the pressure applied to the sensor increases. When no pressure is applied to the FSR, its resistance is very high (in the megaohm range). When pressure is applied, the resistance decreases; the more pressure applied, the lower the resistance.

![](https://hackmd.io/_uploads/Syzk4oVK3.jpg)

**Figure 6**: *LEDs*. 

Red and green LEDs are used to visualize the signals for audio output in speaker mode or headphone mode. Green represents headphone mode, while red represents speaker mode.

![](https://hackmd.io/_uploads/Hk874sEF3.jpg)

**Figure 7**: *10k Resistor*.

This carbon film resistor with a resistance of 10kohm is used in the circuit.

---

## Computer Setup

The initial choice for an IDE was VSCode, but due to connectivity and Pymakr issues, I switched to Thonny, which is a popular IDE for microcontrollers and was suggested in the Raspberry Pi Pico official "Getting Started" guide. Thonny is easy to use and can run local Python code as well as Python 3.

**1. Installing Thonny**\
[Download Thonny](https://github.com/thonny/thonny/releases/tag/v4.1.1)
Thonny comes with Python 3.10 built-in, so a single installer is all that is needed to get started.

**2. Updating Microcontroller Firmware**
The Raspberry Pi Pico WH microcontroller firmware can be updated through Thonny. By pressing the onboard bootsel button and connecting the USB cable to the computer, the Pico WH enters flash memory mode. From there, Thonny can be used to update the firmware, which installs MicroPython.

Here's a quick GIF for better understanding:
![](https://hackmd.io/_uploads/rkDegc4K3.gif)

**3. Installing Pyserial:**
In PowerShell, run the following command to install Pyserial:
```
pip3 install pyserial
```
![](https://hackmd.io/_uploads/Hy4nlqEY3.png)

**4. Installing firmware for the OLED screen:**

![](https://hackmd.io/_uploads/Bye7GcVY3.gif)

---

The following programs will be used in later parts of the project.

**5. Installing Node.js and npm:**

Here's a short blog that explains how to install npm and Node.js:
[Link](https://medium.com/devops-with-valentine/how-to-install-node-js-and-npm-on-windows-10-windows-11-139442f90f12)

**6. Installing Node-RED**

To install Node-RED, open PowerShell and run the following command:
```
npm install -g --unsafe-perm node-red
```



**7. Installing NirCmd**

NirCmd is used to identify available output devices and switch between them for audio output. 

You can download NirCmd from the following link: [Download NirCmd](https://www.nirsoft.net/utils/nircmd.html#:~:text=Full%20Help%20File-,Download%20NirCmd,-Download%20NirCmd%2064)

After downloading NirCmd, copy it to the Windows OS directory by unzipping the file and running the `nircmd.exe` file in administrator mode. This will copy NirCmd to the Windows directory so that it can be easily accessed from the command line without specifying the full path.

![](https://hackmd.io/_uploads/H17VlnNY2.png)

---

## Putting Everything Together

![](https://hackmd.io/_uploads/HJYmi9EY2.jpg)

**Figure 8**: **Wiring**.

The primary sensor used in this project is the Force-Sensing Resistor (FSR) connected to the GP26 pin on the Pico. This connection allows the Pico to measure the resistance of the FSR, translating that resistance into an analog value based on the amount of pressure applied to the FSR.

This project also includes visual feedback through two LEDs, red and green, connected to the GP3 and GP4 pins, respectively. These LEDs indicate the current state of the system, with the red LED illuminating when the FSR reading falls below a certain threshold and the green LED lighting up when the reading exceeds this threshold. The use of these two LEDs provides an intuitive and immediate visual understanding of the system's state, significantly enhancing the user experience.

Furthermore, the system integrates an I2C interface connected to a display, most likely an OLED display equipped with the SSD1306 driver. The I2C interface uses the GP8 and GP9 pins for data (SDA) and clock (SCL), respectively. This display serves to provide real-time, detailed information about the system, such as the exact reading of the FSR, supplementing the binary feedback provided by the LEDs.

---

## Platform

***Node-RED*** is used to visualize the data in this project. Node-RED is a powerful, open-source programming tool for wiring together hardware devices, APIs, and online services in new and interesting ways. It provides a visual, flow-based interface for creating IoT applications, simplifying the process of setting up complex, connected systems.

As mentioned earlier, this platform is self-hosted, meaning no additional fees are required other than the operational cost of the host machine.

![](https://hackmd.io/_uploads/S1TUwo4Y3.png)

**Figure 9**: Node-RED input options.

Node-RED can receive packets from the microcontroller through UDP, TCP, MQTT, and a few other options. In this project, UDP is used due to its ease of use. Furthermore, other options don't offer noticeable differences in our use case. The UDP message will contain a JSON-formatted message.

Here, I found that Node-RED does not come with pre-installed palettes. To use the gauge, I installed a custom widget for the dashboard called "artless-gauge." After starting Node-RED with PowerShell using the command `node-red`, the following steps were taken to install two additional palettes:
1. Click the menu button in the top right corner.
2. Go to "Manage palette."
3. Install the following palettes:
   - node-red-contrib-ui-artless-gauge
   - node-red-dashboard

![](https://hackmd.io/_uploads/BkH5tjNYh.png)

**Figure 10**: Node-RED palettes

---

## The Code

There are four Python scripts used for the project:
1. Script for listing the available audio devices locally
2. Local Python script for changing the audio output
3. Code that runs on the microcontroller for analog signal
4. Code that runs on the microcontroller for the web server

**1. Listing the Audio Output Devices:**
A local Python script is used to find out the available audio output devices. Windows already has some onboard output devices.

```python
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
```

Running this script displays the available audio devices. I used this information to find the device names for my specific use case.

:speech_balloon: To understand which devices are useful, double-checking with the Windows Sound Driver for details was helpful.
![](https://hackmd.io/_uploads/SkxIM2NFn.png)

**2. Microcontroller Code for Web Server:**

A separate MicroPython script is used to send data through UDP for Node-RED to listen to. UDP is used because it is run locally for personal use. The information gathered here is non-sensitive and lightweight, but a constant connection is necessary. UDP fulfills these requirements.

```python=
import network
from time import sleep
import usocket as socket
import ujson

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import machine

ssid = 'router2.4'  # Router Name
password = '12345678'  # Password

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def sendData(message):
    try:
        addr = socket.getaddrinfo('192.168.0.164', 1880)[0][-1]  # ip address:192.168.0.164, port:1880
        s.sendto(message, addr)
        print('Message sent.')
    except:
        print('Message not sent. Error: {str(e)}')


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
```

**3. Microcontroller Main Code for Analog Signal:**

The FSR is used to report the pressure difference when the headphone is lifted versus when the headphone is resting on the headphone stand. Some important points to mention:

:speech_balloon: UART is used to send the signal to the desktop (a Windows machine). GPIO1 and GPIO2 are used for this purpose, so it is important to leave those pins empty on the microcontroller.

The FSR reading is compared with an arbitrary number, 17000. During initial testing, it was found that when the headphone is resting, the pressure reading was around "~24000 units," whereas it was around "~12000 units" when the headphone is lifted. So, 17000 was used as a middle ground.

```python=
from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin

Here is a corrected version of the code with improved grammar:

```python
from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin = ADC(Pin(26))  # FSR is connected to GP26
red_LEDpin = Pin(3, Pin.OUT)
green_LEDpin = Pin(4, Pin.OUT)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

uart = UART(0, 9600)  # UART setup

def display_mapping(fsr_reading):
    oled.fill(0)
    oled.text("FSR Reading:", 0, 10)
    oled.text(str(fsr_reading), 10, 30)
    oled.show()

if __name__ == "__main__":
    print(connect())
    connect()

    while True:
        fsrReading = fsrAnalogPin.read_u16()
        sendData(str(fsrReading))
        print("FSR Reading: ", fsrReading)

        uart.write(f"FSR Reading: {fsrReading}\n")

        if fsrReading < 17000:
            red_LEDpin.value(1)
            green_LEDpin.value(0)
            sleep(1)
        else:
            red_LEDpin.value(0)
            green_LEDpin.value(1)
            sleep(1)

        display_mapping(fsrReading)

        sleep(0.1)
```

In this code, the grammar and punctuation have been corrected.
**Shoeb Chowdhury / SC222RF**

**Shoeb Chowdhury / SC222RF**

A Smart Headphone Stand that switches audio output using FSR (Force Sensitive Resistor).


**Amount of time required to replicate the project:** ~2 hours

## Objective

![](https://hackmd.io/_uploads/r1WOs5NF3.jpg)

The goal of the "AudioMorph" project is to create a smarter sound system. Using a pressure-sensitive resistor (FSR) and a Raspberry Pi Pico WH, the aim was to automatically switch the computer's audio output between speakers and headphones based on whether the headphones are resting on the headphone stand or not. I found it very interesting and intuitive that many TWS (True Wireless Stereo) earphones were able to achieve this for smartphones, but there wasn't any such solution available for desktop users with headphones. So, my goal was to create something for myself.

---

## Materials Used

Component | Link | Bought at | Price* 
-| -| -| -
Raspberry Pi Pico WH |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/)| electrokit.com | 399 SEK**
Jumper wires         |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Breadboard          |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Micro USB cable      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Headphone Stand | [link](https://www.amazon.se/dp/B071S5JH2R?psc=1&ref=ppx_yo2ov_dt_b_product_details)|amazon.se | 99 SEK*
SD1306 0.9" OLED screen               |[link](https://www.amazon.se/dp/B01L9GC470?psc=1&ref=ppx_yo2ov_dt_b_product_details)| amazon.se | 76 SEK*
FSR (Pressure-Sensitive Resistor) 0.5"       |     [link](https://www.electrokit.com/produkt/tryckkansligt-motstand-0-5/)| electrokit.com | 79 SEK*
10k Resistor      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 1 SEK**
LEDs      |[Starter Kit](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 10 SEK**


\* All prices are approximate.

\** Components were part of a kit, so they may be cheaper when bought individually.

---

![](https://hackmd.io/_uploads/rkE3zjVYn.jpg)

**Figure 1**: *Raspberry Pi Pico WH*. 

The microcontroller used in this project is responsible for reading data from the FSR and determining the necessary audio output switch based on the pressure detected.

![](https://hackmd.io/_uploads/rJRKMsVK3.jpg)

**Figure 2**: *SD1306 0.9" OLED screen*. 

This device is used to display the readings of the analog reading and other animations.

![](https://hackmd.io/_uploads/Byezzj4Y3.jpg)

**Figure 3**: *Jumper wires*. 

These wires are used to connect the Raspberry Pi Pico to the FSR and provide power.

![](https://hackmd.io/_uploads/HyIUGj4t2.jpg)

**Figure 4**: *Breadboard*. 

The breadboard serves as a base for connections and allows for easy assembly and disassembly of the system.

![](https://hackmd.io/_uploads/BkKXQoEK3.jpg)

**Figure 5**: *FSR402 Pressure-Sensitive Resistor 0.5"*. 

The FSR consists of a layer of polymer sandwiched between two conductive layers. This polymer layer decreases in resistance as the pressure applied to the sensor increases. When no pressure is applied to the FSR, its resistance is very high (in the megaohm range). When pressure is applied, the resistance decreases; the more pressure applied, the lower the resistance.

![](https://hackmd.io/_uploads/Syzk4oVK3.jpg)

**Figure 6**: *LEDs*. 

Red and green LEDs are used to visualize the signals for audio output in speaker mode or headphone mode. Green represents headphone mode, while red represents speaker mode.

![](https://hackmd.io/_uploads/Hk874sEF3.jpg)

**Figure 7**: *10k Resistor*.

This carbon film resistor with a resistance of 10kohm is used in the circuit.

---

## Computer Setup

The initial choice for an IDE was VSCode, but due to connectivity and Pymakr issues, I switched to Thonny, which is a popular IDE for microcontrollers and was suggested in the Raspberry Pi Pico official "Getting Started" guide. Thonny is easy to use and can run local Python code as well as Python 3.

**1. Installing Thonny**\
[Download Thonny](https://github.com/thonny/thonny/releases/tag/v4.1.1)
Thonny comes with Python 3.10 built-in, so a single installer is all that is needed to get started.

**2. Updating Microcontroller Firmware**
The Raspberry Pi Pico WH microcontroller firmware can be updated through Thonny. By pressing the onboard bootsel button and connecting the USB cable to the computer, the Pico WH enters flash memory mode. From there, Thonny can be used to update the firmware, which installs MicroPython.

Here's a quick GIF for better understanding:
![](https://hackmd.io/_uploads/rkDegc4K3.gif)

**3. Installing Pyserial:**
In PowerShell, run the following command to install Pyserial:
```
pip3 install pyserial
```
![](https://hackmd.io/_uploads/Hy4nlqEY3.png)

**4. Installing firmware for the OLED screen:**

![](https://hackmd.io/_uploads/Bye7GcVY3.gif)

---

The following programs will be used in later parts of the project.

**5. Installing Node.js and npm:**

Here's a short blog that explains how to install npm and Node.js:
[Link](https://medium.com/devops-with-valentine/how-to-install-node-js-and-npm-on-windows-10-windows-11-139442f90f12)

**6. Installing Node-RED**

To install Node-RED, open PowerShell and run the following command:
```
npm install -g --unsafe-perm node-red
```



**7. Installing NirCmd**

NirCmd is used to identify available output devices and switch between them for audio output. 

You can download NirCmd from the following link: [Download NirCmd](https://www.nirsoft.net/utils/nircmd.html#:~:text=Full%20Help%20File-,Download%20NirCmd,-Download%20NirCmd%2064)

After downloading NirCmd, copy it to the Windows OS directory by unzipping the file and running the `nircmd.exe` file in administrator mode. This will copy NirCmd to the Windows directory so that it can be easily accessed from the command line without specifying the full path.

![](https://hackmd.io/_uploads/H17VlnNY2.png)

---

## Putting Everything Together

![](https://hackmd.io/_uploads/HJYmi9EY2.jpg)

**Figure 8**: **Wiring**.

The primary sensor used in this project is the Force-Sensing Resistor (FSR) connected to the GP26 pin on the Pico. This connection allows the Pico to measure the resistance of the FSR, translating that resistance into an analog value based on the amount of pressure applied to the FSR.

This project also includes visual feedback through two LEDs, red and green, connected to the GP3 and GP4 pins, respectively. These LEDs indicate the current state of the system, with the red LED illuminating when the FSR reading falls below a certain threshold and the green LED lighting up when the reading exceeds this threshold. The use of these two LEDs provides an intuitive and immediate visual understanding of the system's state, significantly enhancing the user experience.

Furthermore, the system integrates an I2C interface connected to a display, most likely an OLED display equipped with the SSD1306 driver. The I2C interface uses the GP8 and GP9 pins for data (SDA) and clock (SCL), respectively. This display serves to provide real-time, detailed information about the system, such as the exact reading of the FSR, supplementing the binary feedback provided by the LEDs.

---

## Platform

***Node-RED*** is used to visualize the data in this project. Node-RED is a powerful, open-source programming tool for wiring together hardware devices, APIs, and online services in new and interesting ways. It provides a visual, flow-based interface for creating IoT applications, simplifying the process of setting up complex, connected systems.

As mentioned earlier, this platform is self-hosted, meaning no additional fees are required other than the operational cost of the host machine.

![](https://hackmd.io/_uploads/S1TUwo4Y3.png)

**Figure 9**: Node-RED input options.

Node-RED can receive packets from the microcontroller through UDP, TCP, MQTT, and a few other options. In this project, UDP is used due to its ease of use. Furthermore, other options don't offer noticeable differences in our use case. The UDP message will contain a JSON-formatted message.

Here, I found that Node-RED does not come with pre-installed palettes. To use the gauge, I installed a custom widget for the dashboard called "artless-gauge." After starting Node-RED with PowerShell using the command `node-red`, the following steps were taken to install two additional palettes:
1. Click the menu button in the top right corner.
2. Go to "Manage palette."
3. Install the following palettes:
   - node-red-contrib-ui-artless-gauge
   - node-red-dashboard

![](https://hackmd.io/_uploads/BkH5tjNYh.png)

**Figure 10**: Node-RED palettes

---

## The Code

There are four Python scripts used for the project:
1. Script for listing the available audio devices locally
2. Local Python script for changing the audio output
3. Code that runs on the microcontroller for analog signal
4. Code that runs on the microcontroller for the web server

**1. Listing the Audio Output Devices:**
A local Python script is used to find out the available audio output devices. Windows already has some onboard output devices.

```python
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
```

Running this script displays the available audio devices. I used this information to find the device names for my specific use case.

:speech_balloon: To understand which devices are useful, double-checking with the Windows Sound Driver for details was helpful.
![](https://hackmd.io/_uploads/SkxIM2NFn.png)

**2. Microcontroller Code for Web Server:**

A separate MicroPython script is used to send data through UDP for Node-RED to listen to. UDP is used because it is run locally for personal use. The information gathered here is non-sensitive and lightweight, but a constant connection is necessary. UDP fulfills these requirements.

```python=
import network
from time import sleep
import usocket as socket
import ujson

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import machine

ssid = 'router2.4'  # Router Name
password = '12345678'  # Password

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def sendData(message):
    try:
        addr = socket.getaddrinfo('192.168.0.164', 1880)[0][-1]  # ip address:192.168.0.164, port:1880
        s.sendto(message, addr)
        print('Message sent.')
    except:
        print('Message not sent. Error: {str(e)}')


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
```

**3. Microcontroller Main Code for Analog Signal:**

The FSR is used to report the pressure difference when the headphone is lifted versus when the headphone is resting on the headphone stand. Some important points to mention:

:speech_balloon: UART is used to send the signal to the desktop (a Windows machine). GPIO1 and GPIO2 are used for this purpose, so it is important to leave those pins empty on the microcontroller.

The FSR reading is compared with an arbitrary number, 17000. During initial testing, it was found that when the headphone is resting, the pressure reading was around "~24000 units," whereas it was around "~12000 units" when the headphone is lifted. So, 17000 was used as a middle ground.

```python=
from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin

Here is a corrected version of the code with improved grammar:

```python
from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin = ADC(Pin(26))  # FSR is connected to GP26
red_LEDpin = Pin(3, Pin.OUT)
green_LEDpin = Pin(4, Pin.OUT)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

uart = UART(0, 9600)  # UART setup

def display_mapping(fsr_reading):
    oled.fill(0)
    oled.text("FSR Reading:", 0, 10)
    oled.text(str(fsr_reading), 10, 30)
    oled.show()

if __name__ == "__main__":
    print(connect())
    connect()

    while True:
        fsrReading = fsrAnalogPin.read_u16()
        sendData(str(fsrReading))
        print("FSR Reading: ", fsrReading)

        uart.write(f"FSR Reading: {fsrReading}\n")

        if fsrReading < 17000:
            red_LEDpin.value(1)
            green_LEDpin.value(0)
            sleep(1)
        else:
            red_LEDpin.value(0)
            green_LEDpin.value(1)
            sleep(1)

        display_mapping(fsrReading)

        sleep(0.1)
```

In this code, the grammar and punctuation have been corrected.
