# Surenoo-4004-LCD-python-code

## Overview
This repository contains Python code to drive the Surenoo 4004 LCD module paired with the PCF8574T I²C backpack (I²C port expander).
The LCD screen + I2C backpack can be found here: https://www.aliexpress.us/item/2251832722412443.html?gatewayAdapt=glo2usa4itemAdapt

## Challenges
This LCD screen is a great 40x4 screen; however, it presents challenges when using standard LCD Python libraries such as [RPLCD](https://pypi.org/project/RPLCD/0.3.0/).
When using this library, only the first 2 rows of characters display, leaving the other 2 rows blank. After further investigation, it was found that the LCD controller (HD44780 controller) can  only address up to 80 characters (half this screen’s capacity). To address
this issue, the manufacturer has 2 LCD controllers, each of which is addressed individually via Enable Pins. 
The manufacturer provides an Arduino library that allows for this, but nothing for Python. The [RPLCD](https://pypi.org/project/RPLCD/0.3.0/) library can only address 1 LCD controller.

## The Solution
After much trial and error, I found the [charlcd library](https://pypi.org/project/charlcd/) by Bartosz Kościów (kosci) that allows for 
addressing the 2 LCD controllers needed. This repo provides the needed libraries and sample code to get started. The Enable Pin 2 needed to be overwritten for this to work. Hope this helps!

## How to use

1. Enable the I2C interface on your device, connect the LCD module to the I²C backpack, and then connect the I²C backpack to the I2C bus.

2. Create and activate a virtual environment:

   - Windows:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

   - Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```



4. Run the example main script:

   ```bash
   python main.py
   ```

## Tags
hardware, lcd, surenoo, surenoo-4004, pcf8574, PCF8574T, i2c, hd44780, python, charlcd, raspberry-pi, arduino, embedded, microcontroller, 40x4, lcd-backpack, i2c-backpack, display, tutorial, SLC4004A, SLC4004B


