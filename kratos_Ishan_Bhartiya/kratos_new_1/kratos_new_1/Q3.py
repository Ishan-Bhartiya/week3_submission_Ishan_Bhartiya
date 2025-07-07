#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from kratos_new_1.msg import Message

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.publisher=self.create_publisher(Message,'Rover_Comm',10)
        self.timer=self.create_timer(10,self.timer_callback)
        
    def timer_callback(self):
        msg=Message()
        self.publisher.publish(msg)	
        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher=MinimalPublisher()
    rclpy.spin(minimal_publisher)
    
if __name__ == '__main__':
    main()
    
