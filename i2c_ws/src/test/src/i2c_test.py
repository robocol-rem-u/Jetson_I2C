from smbus2 import SMBus
import time

# Open i2c bus 1 and read one byte from address 80, offset 0
with SMBus(1) as bus:
    # Write a byte to address 80, offset 0
    while True : 
        address = 0x20
        data = 0xFF
        bus.write_byte_data(address, 0, data)
        time.sleep(0.2)
        bus.write_byte_data(address, 0,0x00 )
        time.sleep(0.2)

