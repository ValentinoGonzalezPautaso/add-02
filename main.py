from machine import ADC
from time import sleep
adc = ADC (26)

while 1:
    val = adc.read_u16()

    val = val * 3.3 / 65535
    temp = val / 0.01
    temp = round (temp, 2)
    print("la temperatura es:{}°C", temp)
    sleep(.5)
