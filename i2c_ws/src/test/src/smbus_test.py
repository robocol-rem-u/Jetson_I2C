import SDL_Pi_INA3221 as ina
import rospy
from std_msgs.msg import String
from rospy.exceptions import ROSInterruptException

ic = ina.SDL_Pi_INA3221(addr = 0x40)

def main():
    rospy.init_node('voltage_monitoring', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher('Robocol/Power/voltages', String)

    while not rospy.is_shutdown():
        """ for i in range(13):
            v = 0
            pub.publish('1:{}'.format(v)) """

        bus_voltage_a = ic.getBusVoltage_V(1)
        bus_voltage_b = ic.getBusVoltage_V(2)
        bus_voltage_c = ic.getBusVoltage_V(3)

        print('-'*10)
        print('bus voltage 1 = {0}\n'.format(bus_voltage_a),
        'bus voltage 2 = {0}\n'.format(bus_voltage_b),
        'bus voltage 3 = {0}\n'.format(bus_voltage_c))

if __name__ == '__main__':
    try:
        main()
    except ROSInterruptException:
        print('F')