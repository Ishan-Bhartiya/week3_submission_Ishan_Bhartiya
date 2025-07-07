#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Publisher')
        self.publisher_=self.create_publisher(String, 'new',10)
        timer_period=1/15
        self.timer=self.create_timer(timer_period,self.timer_callback)
	
    def timer_callback(self):
        msg=String()
        msg.data='Hello World !'
        self.publisher_.publish(msg)
    	
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher=MinimalPublisher()
    rclpy.spin(minimal_publisher)
    


if __name__ == '__main__':
    main()
