from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin = ADC(Pin(26))  # FSR is connected to GP26
red_LEDpin = PWM(Pin(3))  # connect Red LED to GP3
green_LEDpin = PWM(Pin(4))  # connect Green LED to GP4

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)  # Adjusted SDA and SCL pins
oled = SSD1306_I2C(128, 64, i2c)

uart = UART(0, 9600)  # UART setup

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def display_mapping(fsr_reading):
    oled.fill(0)
    oled.text("FSR Reading:", 0, 10)
    oled.text(str(fsr_reading), 10, 30)
    oled.show()


if __name__=="__main__":
    print(connect())
    connect()
    sendData(fsrAnalogPin.read_u16())
    while True:
        fsrReading = fsrAnalogPin.read_u16()
        print("Analog reading = ", fsrReading)

        uart.write(f'FSR Reading: {fsrReading}\n')

        if fsrReading < 1000:  # Adjust this threshold as needed
            red_LEDpin.duty_u16(65535)  # Red LED fully ON
            green_LEDpin.duty_u16(0)  # Green LED OFF
           
        else:
            green_LEDpin.duty_u16(65535)  # Green LED fully ON
            red_LEDpin.duty_u16(0)  # Red LED OFF
            LEDbrightness = map(fsrReading, 500, 65535, 0, 65535)
            
        display_mapping(fsrReading)

        sleep(0.1)

