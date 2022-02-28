#!/usr/bin/env python
import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String

def main():
    rospy.init_node('Potencia', anonymous=True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher('Robocol/Power/voltages', String, queue_size=10)

    while not rospy.is_shutdown():
        for i in range(12):
            v = i
            pub.publish('1:{}'.format(v))
        
        rate.sleep()



if __name__== '__main__':
    try:
        main()
    except ROSInterruptException:
        print('fail')
