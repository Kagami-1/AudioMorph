# AudioMorph: FSR-Enabled Sound System Routing
**Shoeb CHowdhury / SC222RF**

A Smart Headphone Stand that switches audio output using FSR(Force Sensetive Resistor)

**Amount of time required to replicate the project: ~1 hour**

# Objective



# Materials used

Component | Part of | Bought at | Price* 
-| -| -| -
Raspberry Pi pico WH |Start Kit – Applied IoT at Linnaeus University (2023) | electrokit.com | 399.00 SEK**
SD1306               || amazon.se | 76 SEK*
Jumper wires         |Start Kit – Applied IoT at Linnaeus University (2023) | electrokit.com | 100 SEK**
Bread board          |Start Kit – Applied IoT at Linnaeus University (2023) | electrokit.com | 100 SEK**
Micro USB cable      |Start Kit – Applied IoT at Linnaeus University (2023) | electrokit.com | 100 SEK**
FSRPressure sensitive resistance 0.5"       || electrokit.com | 76 SEK*
HeadPhone Stand ||amazon.se | 99 SEK*

\* All prices are approximated.

\** Components were part of a kit, thus they may be cheaper when bought individually.

---

**Figure 1**: pi pico wh. 

<img style="display:block; padding:1px;border:1px #eee;width:22%;" src="./images/pi pico WH.png" />

The microcontroller used in this project. It is responsible for reading data from the FSR and determining the necessary audio output switch based on the pressure detected.

**Figure 2**: sd1306. 

<img style="display:block; padding:1px;border:1px #eee;width:25%;" src="./images/sd1306.png" />

Device to display the readings of the analogue reading and other animations


**Figure 3**: Jumper wires. 

<img style="display:block; padding:1px;border:1px #eee;width:20%;" src="./images/JumperWires.png" />

Used to connect the Raspberry Pi Pico to the FSR and to provide power.

**Figure 4**: Breadboard. 

<img style="display:block; padding:1px;border:1px #eee;width:30%;" src="./images/BreadBoard.png" />

Serves as a base for connections and allows for easy assembly and disassembly of the system

**Figure 5**: FSRPressure sensitive resistance 0.5". 

<img style="display:block; padding:1px;border:1px #eee;width:20%;" src="./images/fsr.png" />

The FSR consists of a layer of polymer sandwiched between two conducive layers. This polymer layer decreases in resistance as the pressure applied to the sensor increases. When no pressure is applied to the FSR, its resistance is very high (in the Megaohms range). When pressure is applied, the resistance decreases; the more pressure applied, the lower the resistance.

# Computer setup 
The initial choice for IDE was VSCode. But after having multiple problems with connectivity I decided to switch to Thonny which is popular IDE for microcontroller and as suggested by the Raspberry Pi pico Getting Started guide. Using Thonny is particularly easy as it can also be used to run local python code as well as python3. Downloading and installing firmware, library for compatible components were also very straightforward and easy.

## Steps - Can be followed on certain Linux distros.

1. Installing Thonny

Link: https://github.com/thonny/thonny/releases/tag/v4.1.1)


2. Updating firmware

Firstly, The raspberry pi pico wh microcontroller firmware is updated through Thonny. After pressing down the onboard bootsel button, pico wh goes to flash memory mode. Thonny -> Run (Menu Bar) -> Configure Interpreter...-> Choose interpreter from the first drop down -> Select: MicroPython (Raspberry Pi Pico)-> Install or update MicroPython-> Target Volume(Select: RPI-RP2)->Variant(Pico WH)->Select version(rp2-pico-w-20230426-v1.20.0)

Secondly, Pyserial on powershell write:
```
pip install pyserial
```
Thirdly, Oled: Thonyy-> Tools -> Manage Packages...->in the search box look up 1306-> install
---

The following programs will be used in later parts of the project.

4. Installing Node-RED
```
npm install -g --unsafe-perm node-red
```


# Putting everything together:

**Figure 6**: Wiring. 

<img style="display:block;margin:1px auto;padding:1px;border:1px #eee;width:100%;" src="./images/wiringAudiomorph.png" />

The primary sensor used in this project is the Force Sensing Resistor (FSR) connected to the GP26 pin on the Pico. This connection allows the Pico to measure the resistance of the FSR, translating that resistance into an analog value based on the amount of pressure applied to the FSR.

This project also includes visual feedback via two LEDs, red and green, connected to the GP3 and GP4 pins respectively. These LEDs indicate the current state of the system, with the red LED illuminating when the FSR reading falls below a certain threshold and the green LED lighting up when the reading exceeds this threshold. The use of these two LEDs provides an intuitive and immediate visual understanding of the system's state, which significantly enhances the user experience.

Furthermore, the system integrates an I2C interface connected to a display, likely an OLED display equipped with the SSD1306 driver. The I2C interface uses the GP8 and GP9 pins for data (SDA) and clock (SCL) respectively. This display serves to provide real-time, detailed information about the system, such as the exact reading of the FSR, supplementing the binary feedback provided by the LEDs.

# Platform

Node red is used to visualise the data in this project. Node-RED is a powerful, open-source programming tool for wiring together hardware devices, APIs, and online services in new and interesting ways. It provides a visual, flow-based interface for creating IoT applications, simplifying the process of setting up complex, connected systems.

As I mentioned above, this platform is self-hosted, meaning no additional fee is required other than the operational cost of the host machine.

**Figure 7**: Node-Red input options. 

<img style="display:block;padding:1px;border:1px #eee;width:80%;" src="./images/Node-RED-Input.png" />

Node-Red can receive packets from the microcontroller through UDP, TCP, MQTT, and a few more options. In this project, the UDP protocol will be used due to its ease of use. Furthermore, other options don't offer a noticeable difference in our use case. The UDP message will contain JSON formatted message. 

**Figure 8**: Node-Red 'function' block. 

<img style="display:block;width:40%;" src="./images/functionBlock.png" />

With the message received at Node-Red, 'function' blocks can be used to filter the specific data from the message. After filtered, 
the message can be sent to chosen dashboard node to be illustrated. Furthermore, as an addendum to showing the data on the dashboard, filtered data can be uploaded to connected MongoDB; Node-Red offers a dedicated block for this. 



