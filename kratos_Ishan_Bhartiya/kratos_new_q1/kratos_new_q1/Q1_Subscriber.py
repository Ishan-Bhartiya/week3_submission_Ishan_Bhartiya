#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Subscriber')
        self.subscriber=self.create_subscription(String,'new',self.listener_callback,10)
        self.subscriber
    
    def listener_callback(self,msg):
        print(msg.data)
    	

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber=MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

if __name__ == '__main__':
    main()
