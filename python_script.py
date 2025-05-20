import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

# Setup
lcd = CharLCD('PCF8574', 0x27)  # Replace 0x27 with your I2C address
sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity

        lcd.clear()
        lcd.write_string(f"Temp: {temp}C")
        lcd.crlf()
        lcd.write_string(f"Humidity: {humidity}%")

        time.sleep(2)

    except RuntimeError as e:
        print(f"Reading error: {e.args[0]}")
        time.sleep(5)
