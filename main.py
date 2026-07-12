##library from https://bitbucket.org/kosci/charlcd/src/master/ , full credit to the author, Bartosz Kościów
from charlcd import buffered as lcd
from charlcd.drivers.i2cm import I2C as I2CM



# I2C address specific to the PCF8574T(or PCF8574) I2C backpack of the Surenoo 4004 LCD Module
i2cm_interface = I2CM(0x27, 1)

#To make the second half of the screen addressible, we need to define that E2 (Enable 2) should address PIN 1.
#This is because the second half of the screen is controlled by a different LCD controller than the default one. 
i2cm_interface.pins['E2'] = 1

lcd_writer = lcd.CharLCD(40, 4, i2cm_interface, 0, 0)

lcd_writer.init()
lcd_writer.stream("""Why do hardware engineers love I2C? Because this brilliant 
                  two-wire protocol allows effortless communication between your chips.
                   It keeps PCB layouts efficient.""")
lcd_writer.flush()



