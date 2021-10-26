from smbus2 import SMBus

# Open i2c bus 1 and read one byte from address 80, offset 0
with SMBus(1) as bus:
    # Write a byte to address 80, offset 0
    data = 0xFF
    bus.write_byte_data(80, 0, data)