#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber_cum_Publisher(Node):
    
    def __init__(self):     
        super().__init__('Subscriber')
        self.subscriber=self.create_subscription(String,'s1',self.listener_callback,10)
        self.subscriber
        
        self.publisher=self.create_publisher(String,'s2',10)
        
    def listener_callback(self,msg):
        Msg = String()
        if msg.data=='Red':
            Msg.data='Green'
            print(Msg.data)
        elif msg.data=='Green':
            Msg.data='Red'
            print(Msg.data)
        self.publisher.publish(Msg)        
        
def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber_cum_publisher=MinimalSubscriber_cum_Publisher()
    rclpy.spin(minimal_subscriber_cum_publisher)

if __name__ == '__main__':
    main()
