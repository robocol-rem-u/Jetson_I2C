#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # rospy.loginfo('I heard ' + data.data)
    print(data.data)

def main():
    rospy.init_node('listener', anonymous= True)
    rospy.Subscriber('chatter',String,callback)
    rospy.spin()
    pass

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print( 'closed')
