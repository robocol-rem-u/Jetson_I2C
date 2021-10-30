# imports: smbus2 for i2c communication through jetson tx2 gpio. See pinout online. 
# rospy for ros melodic integration
# string for communication with REM-u interface
from smbus2 import SMBus
import smbus2 
import rospy
from std_msgs.msg import String

# open i2c bus 1
bus = SMBus(1)

#addresses for the two INA3221 IC breakout boards
address_a = 0x40
address_b = 0x41

# manufacturer id register pointer
id = 0xFF

# bus voltage registers
bus_v1 = 0x2
bus_v2 = 0x4
bus_v3 = 0x6
#jsjsjs 


def main_i2c():
    while not rospy.is_shutdown:
        v1 = bus.read_block_data(bus,bus_v1)
        print(v1)
        pass

if __name__ == '__main__':
	try:
		main_i2c()
	except rospy.ROSInterruptException:
		print('Node murdered')