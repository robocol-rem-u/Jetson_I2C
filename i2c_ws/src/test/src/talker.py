#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def main_loop():
    rospy.init_node('talker', anonymous= True)
    rate = rospy.Rate(10)
    pub = rospy.Publisher('chatter', String, queue_size=10)

    while not rospy.is_shutdown():
        pub.publish('lmao')
        rate.sleep()

if __name__ == '__main__':
    try: 
        main_loop()
    except rospy.ROSInterruptException :
        print('lmao')
