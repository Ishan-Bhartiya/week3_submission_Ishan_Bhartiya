#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.publisher_1 = self.create_publisher(Int32,'second',10)
        self.publisher_2 = self.create_publisher(Int32,'minute',10)
        self.publisher_3 = self.create_publisher(Int32,'hour',10)
        self.publisher_4 = self.create_publisher(String,'clock',10)
        
        self.timer = self.create_timer(1,self.timer_callback)
        self.s=0
        self.m=0
        self.h=0
        
    def timer_callback(self):
        second=Int32()
        minute=Int32()
        hour=Int32()
        time=String()
        
        second.data = self.s
        minute.data = self.m
        hour.data = self.h
        time.data = str(hour.data)+":"+str(minute.data)+":"+str(second.data)
        
        self.s=self.s+1
        if self.s==60:
            self.s=0
            self.m+=1
            if self.m==60:
                self.m=0
                self.h+=1
        
        
        self.publisher_1.publish(second)
        self.publisher_2.publish(minute)
        self.publisher_3.publish(hour)
        self.publisher_4.publish(time)
        print(time.data)
        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher=MinimalPublisher()
    rclpy.spin(minimal_publisher)


if __name__ == '__main__':
    main() 
