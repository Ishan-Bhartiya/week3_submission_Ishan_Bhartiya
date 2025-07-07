#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.publisher=self.create_publisher(String, 's1',10)
        timer_period=10
        self.timer=self.create_timer(timer_period,self.timer_callback)
        self.i=0
	
    def timer_callback(self):
        self.i+=1
        msg=String()
        if (self.i)%2!=0:
            msg.data='Red'
        elif (self.i)%2==0:
            msg.data='Green'
        self.publisher.publish(msg)
        print(msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher=MinimalPublisher()
    rclpy.spin(minimal_publisher)


if __name__ == '__main__':
    main()
