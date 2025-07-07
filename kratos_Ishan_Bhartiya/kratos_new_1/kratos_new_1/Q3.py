#!/usr/bin/env python3 #Shebang for python files
#Imporring requried libraries and modules
import rclpy
from rclpy.node import Node
from kratos_new_1.msg import Message

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher')#Naming the node as Publisher
        self.publisher=self.create_publisher(Message,'Rover_Comm',10)#Creating publisher object, which publishes the custom Message type object over the topic 'Rover_Comm'
        self.timer=self.create_timer(10,self.timer_callback)#Creates timer object, which calls the timer_callback function every 10 seconds
        
    def timer_callback(self):
        msg=Message()#Creates a custom message type object
        self.publisher.publish(msg)	#Publishes the message
        
def main(args=None):
    rclpy.init(args=args)#Initialises the rclpy python library
    minimal_publisher=MinimalPublisher()#Creates an instance of the MinimalPublisher class
    rclpy.spin(minimal_publisher)#Keeps running the above created instance unless stopped
    
if __name__ == '__main__':#Sets __name__ to '__main__' if the file is called directly to be run, otherwise not
    main()                #Doing the above prevents the file from running if it is called as a module into another script
    
