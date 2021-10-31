import rospy
from std_msgs.msg import String

def main_loop():
    rospy.init_node('talker', anonymous= True)
    pub = rospy.Publisher('chatter', String, queue_size=1)

    while not rospy.is_shutdown:
        pub.publish('lmao')
        rospy.sleep()

if __name__ == '__main__':
    try: 
        main_loop
    except rospy.ROSInterruptException :
        print('lmao')
