****[to the peer reviewers]Sorry for the delay I expect it to be done with it by tonight-midnight 6th july****

**Shoeb Chowdhury / SC222RF**

A Smart Headphone Stand that switches audio output using FSR(Force Sensetive Resistor)


**Amount of time required to replicate the project: ~2 hour**

# Objective

![](https://hackmd.io/_uploads/r1WOs5NF3.jpg)


# Materials used

Component | Link | Bought at | Price* 
-| -| -| -
Raspberry Pi pico WH |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/)| electrokit.com | 399 SEK**
Jumper wires         |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Bread board          |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
Micro USB cable      |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 100 SEK**
HeadPhone Stand | [link](https://www.amazon.se/dp/B071S5JH2R?psc=1&ref=ppx_yo2ov_dt_b_product_details)|amazon.se | 99 SEK*
SD1306 0.9" OLED screen               |[link](https://www.amazon.se/dp/B01L9GC470?psc=1&ref=ppx_yo2ov_dt_b_product_details)| amazon.se | 76 SEK*
FSRPressure sensitive resistance 0.5"       |     [link](https://www.electrokit.com/produkt/tryckkansligt-motstand-0-5/)| electrokit.com | 79 SEK*
10k Resistor      |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 1 SEK**
LEDs      |[Starter Kit ](https://www.electrokit.com/produkt/start-kit-applied-iot-at-linnaeus-university-2023/) | electrokit.com | 10 SEK**






\* All prices are approximated.

\** Components were part of a kit, thus they may be cheaper when bought individually.

---

![](https://hackmd.io/_uploads/rkE3zjVYn.jpg)

**Figure 1**: *Raspberry pi pico wh*. 



The microcontroller used in this project. It is responsible for reading data from the FSR and determining the necessary audio output switch based on the pressure detected.

![](https://hackmd.io/_uploads/rJRKMsVK3.jpg)

**Figure 2**: *sd1306 oled screen 0.96"*. 


Device to display the readings of the analogue reading and other animations


![](https://hackmd.io/_uploads/Byezzj4Y3.jpg)

**Figure 3**: Jumper wires. 


Used to connect the Raspberry Pi Pico to the FSR and to provide power.

![](https://hackmd.io/_uploads/HyIUGj4t2.jpg)


**Figure 4**: Breadboard. 

Serves as a base for connections and allows for easy assembly and disassembly of the system

![](https://hackmd.io/_uploads/BkKXQoEK3.jpg)


**Figure 5**: FSR402 Pressure sensitive resistance 0.5". 

The FSR consists of a layer of polymer sandwiched between two conducive layers. This polymer layer decreases in resistance as the pressure applied to the sensor increases. When no pressure is applied to the FSR, its resistance is very high (in the Megaohms range). When pressure is applied, the resistance decreases; the more pressure applied, the lower the resistance.


![](https://hackmd.io/_uploads/Syzk4oVK3.jpg)

**Figure 6**: LED. 
Red and Green LED were used to visualise the signals where if the Audio Output is in Speaker mode or Headphone mode. Green would mean headphone and Red being Speaker.


![](https://hackmd.io/_uploads/Hk874sEF3.jpg)

**Figure 6**: 10k Resistor

Carbon film resistor 0.25W 10kohm (10k)\
Color code: brown black orange gold\
Size: body ø2.5×6.8mm\
legs each ø0.54x28mm\
Tolerance: 5%\


---



# Computer setup 
The initial choice for IDE was VSCode. But after having multiple problems with connectivity and Pymakr I decided to switch to Thonny which is popular IDE for microcontroller and as suggested by the Raspberry Pi pico official "Getting Started" guide. Using Thonny is particularly easy as it can also be used to run local python code as well as python3. Downloading and installing firmware, library for compatible components were also very straightforward only buttons press away.


**1. Installing Thonny**

[Download Thonny](https://github.com/thonny/thonny/releases/tag/v4.1.1)

Easy to get started. Thonny comes with Python 3.10 built in, so just one simple installer is needed and you're ready to learn programming.

**2. Updating Microcontroller firmware**

*Firstly*, The raspberry pi pico wh microcontroller firmware is updated through Thonny. After pressing down the onboard bootsel button, pico wh goes to flash memory mode. 
Heres a quick gif for better understanding:

![](https://hackmd.io/_uploads/rkDegc4K3.gif)

Thonny -> 
Run (Menu Bar) -> 
Configure Interpreter...-> 
Choose interpreter from the first drop down -> 
Select: MicroPython (Raspberry Pi Pico)-> 
Install or update MicroPython-> 
Target Volume(Select: RPI-RP2)->
Variant(Pico WH)->Select version(rp2-pico-w-20230426-v1.20.0)




**3. Installing Pyserial:**

In powershell write
```
pip install pyserial
```
![](https://hackmd.io/_uploads/Hy4nlqEY3.png)



**4. Installing firmware for the oled screen:**

![](https://hackmd.io/_uploads/Bye7GcVY3.gif)





---

The following programs will be used in later parts of the project.


**5. Installing nodejs and npm:**

Heres, a short blog that explain how to install npm and nodejs

[Link](https://medium.com/devops-with-valentine/how-to-install-node-js-and-npm-on-windows-10-windows-11-139442f90f12)

**7. Installing Node-RED**

Boot up powershell and write this code
```
npm install -g --unsafe-perm node-red
```




# Putting everything together:

![](https://hackmd.io/_uploads/HJYmi9EY2.jpg)




**Figure 6**: Wiring. 



The primary sensor used in this project is the Force Sensing Resistor (FSR) connected to the GP26 pin on the Pico. This connection allows the Pico to measure the resistance of the FSR, translating that resistance into an analog value based on the amount of pressure applied to the FSR.
![](https://hackmd.io/_uploads/H1Adu9Eth.jpg)
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
the message can be sent to chosen dashboard node to be illustrated. 




