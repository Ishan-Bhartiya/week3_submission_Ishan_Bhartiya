#!/usr/bin/env python3 #Shebang for python filse
#Importing necessary libraries and modules
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber_cum_Publisher(Node):
    
    def __init__(self):     
        super().__init__('Subscriber')#Naming the node Subscriber
        self.subscriber=self.create_subscription(String,'s1',self.listener_callback,10)#Creating Subscriber Object, listens to what is published on the topic s1
        self.subscriber #Prevents warnings on unused variables
        
        self.publisher=self.create_publisher(String,'s2',10) #Creates publisher object, which publishes String type message on the topic s2
        
    def listener_callback(self,msg):
        Msg = String() #Creates string type object
        ''' if this node receives 'Red' on topic s1 it publishes 'Green' on topic s2, and if it receives Green on s1, then it publishes Red on s2
        '''
        if msg.data=='Red':
            Msg.data='Green'
            print(Msg.data)
        elif msg.data=='Green':
            Msg.data='Red'
            print(Msg.data)
        self.publisher.publish(Msg)    #Publishes the Msg to topic s2    
        
def main(args=None):
    rclpy.init(args=args) #Initialises rclpy Python library
    minimal_subscriber_cum_publisher=MinimalSubscriber_cum_Publisher()#Createsan instance of the MinimalSubscriber class
    rclpy.spin(minimal_subscriber_cum_publisher)# Keeps running the above instance unless stopped

if __name__ == '__main__': #Sets __name__ to '__main__ if the file is run directly, and not if it is imported as amodule into another script
    main()                 #Doing so helps running the file only if it is called to be run
