from smbus2 import SMBus
import time
import rospy

# Open i2c bus 1 and read one byte from address 80, offset 0

def main_i2c():

    rospy.init_node('i2c_test', anonymous=True) #Inicio nodo
    rate = rospy.Rate(10) #10hz
    
    pub = rospy.Publisher('Robocol/Potencia/voltages')
    with SMBus(1) as bus:
        # Write a byte to address 80, offset 0
        while not rospy.is_shutdown():
            address = 0x20
            data = 0xFF
            bus.write_byte_data(address, 0, data)
            time.sleep(0.2)
            bus.write_byte_data(address, 0,0x00 )
            time.sleep(0.2)
            
            rate.sleep()

if __name__ == '__main__':
	try:
		main_i2c()
	except rospy.ROSInterruptException:
		print('Nodo detenido')