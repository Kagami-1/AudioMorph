from machine import Pin, ADC, PWM, I2C, UART
from ssd1306 import SSD1306_I2C
from time import sleep
from web_server import connect
from web_server import sendData

fsrAnalogPin = ADC(Pin(26))  # FSR is connected to GP26
LEDpin = PWM(Pin(3))  # connect Red LED to GP6

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
    while True:
        fsrReading = fsrAnalogPin.read_u16()
        print("Analog reading = ", fsrReading)

        uart.write(f'FSR Reading: {fsrReading}\n')
        

        if fsrReading < 1000:  # Adjust this threshold as needed
            LEDpin.duty_u16(0)
            sendData("headphone lifted")
        else:
            LEDbrightness = map(fsrReading, 500, 65535, 0, 65535)
            LEDpin.duty_u16(int(LEDbrightness))

        display_mapping(fsrReading)

        sleep(0.1)
    
