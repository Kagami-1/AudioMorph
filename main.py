from machine import Pin, ADC, PWM, UART
from time import sleep

fsrAnalogPin = ADC(Pin(26))  # FSR is connected to GP26
LEDpin = PWM(Pin(4))  # connect Red LED to GP0

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

uart = UART(0, 9600)

while True:
    fsrReading = fsrAnalogPin.read_u16()
    #print("Analog reading = ", fsrReading)

    # if the reading is less than a threshold, turn off the LED
    if fsrReading < 1000:  # Adjust this threshold as needed
        LEDpin.duty_u16(0)
        uart.write('headphones lifted\n')
    else:
        # we'll need to change the range from the analog reading (0-65535) down to the range
        # used by duty_u16 (0-65535) with map!
        LEDbrightness = map(fsrReading, 500, 65535, 0, 65535)
        # LED gets brighter the harder you press
        LEDpin.duty_u16(int(LEDbrightness))

    sleep(0.1)