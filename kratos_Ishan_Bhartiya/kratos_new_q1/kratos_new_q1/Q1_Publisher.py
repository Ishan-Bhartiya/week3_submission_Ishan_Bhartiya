#!/usr/bin/env python3      #Shebang for a python filere
#importing required libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Publisher')
        self.publisher_=self.create_publisher(String, 'new',10) #Creating publisher object, which publishes String type variable on the topic new
        timer_period=1/15
        self.timer=self.create_timer(timer_period,self.timer_callback) #Creating timer object,calls the timer_callback function every 1/15 seconds
	
    def timer_callback(self):
        msg=String() #Creating a string objct
        msg.data='Hello World !'
        self.publisher_.publish(msg)#Publishes the msg over the topic
    	
def main(args=None):
    rclpy.init(args=args) #initializes the ROS 2 Python client library, which is rclpy
    minimal_publisher=MinimalPublisher()  #Creating an instance of the MinimalPublisher class
    rclpy.spin(minimal_publisher) #Keeps running minimal publisher unless stopped
    


if __name__ == '__main__':   #Runs the whole programme(sets __name__ to '__main__') if run directly, not if it's imported as a module into another script
    main()
