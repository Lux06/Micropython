from machine import Pin, I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 32, i2c)

oled.text('INGENIERIA', 0, 2)
oled.text('ROBOTICA', 0, 20)
oled.show()
