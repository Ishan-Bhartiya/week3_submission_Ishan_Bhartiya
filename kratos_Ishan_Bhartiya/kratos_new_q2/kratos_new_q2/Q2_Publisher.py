#!/usr/bin/python3 #Shebang for running python files
#Importing necessary modules and libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher') #Naming the node Publisher
        self.publisher=self.create_publisher(String, 's1',10) #Creating Publisher object, publishes string type message on the topic 's1'
        timer_period=10
        self.timer=self.create_timer(timer_period,self.timer_callback)#Creating timer object, calls timer_callback every 10 seconds
        self.i=0 
	
    def timer_callback(self):
        ''' i is incremented in every iteration, every time i is odd, the data field of the message object(msg) sent contains the string 'Red', and it containts 'Green' when i is even
	'''
        self.i+=1                  
        msg=String() #Creating message object of string datatype
        if (self.i)%2!=0:
            msg.data='Red'
        elif (self.i)%2==0:
            msg.data='Green'
        self.publisher.publish(msg) #Publishes message
        print(msg.data)
        
def main(args=None):
    rclpy.init(args=args) #Initialises the rclpy python library
    minimal_publisher=MinimalPublisher() #Creates an instance of the MinimalPublisher class
    rclpy.spin(minimal_publisher) #Keeps running the minimal_publisher object unless stopped


if __name__ == '__main__': #If the file is to be run directly, __name__ is set to '__main__, thereby running it, but this doesn't happen when the file is imported as a module in another script,so it cannot run
    main()
