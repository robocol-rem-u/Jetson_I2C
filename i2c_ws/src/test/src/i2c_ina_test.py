#!/usr/bin/env python
from smbus2 import SMBus
import rospy
from rospy.topics import Topic
from std_msgs.msg import String

# open i2c bus 1
bus = SMBus(1)

#addresses for the two INA3221 IC breakout boards
address_a = 0x40
address_b = 0x41

# manufacturer id register pointer
id_reg = 0xFF

# bus voltage registers
bus_v1 = 0x2
bus_v2 = 0x4
bus_v3 = 0x6
#jsjsjs 


def main_i2c():
    id = bus.read_word_data(address_a, id_reg)
    print("Volage monitoring with TI INA3221.\n"
        "Getting manufacturer id from register 0xFF... {0}".format(id))
    
    topic = 'Robocol/Power/voltages'
    rospy.init_node('Power_sense', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher(topic, String,queue_size=10)

    while not rospy.is_shutdown:
        v1 = bus.read_word_data(bus,bus_v1)
        pub.publish('1:{}'.format(v1))
        print(v1)
        rate.sleep()
        

if __name__ == '__main__':
	try:
		main_i2c()
	except rospy.ROSInterruptException:
		print('Node murdered')