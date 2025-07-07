#!/usr/bin/env python3    #Shebang for any python file
 #Importing necessary libraries and modules
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Subscriber') #Sets this node's name to Subscriber
        self.subscriber=self.create_subscription(String,'new',self.listener_callback,10)  #Creates subsciber object, receives String type message and then calls listener_callback
        self.subscriber  #Prevents warnings on unused variables
    
    def listener_callback(self,msg): 
        print(msg.data)                #Prints the data field of the message object
    	

def main(args=None):
    rclpy.init(args=args) #Initialises rclpy python library
    minimal_subscriber=MinimalSubscriber() #creates an instance of the MinimalSubscriber class
    rclpy.spin(minimal_subscriber) #Keeps on running the MinimalSubscriber till stopped

if __name__ == '__main__': #Sets __name__ to '__main__' if run directly, not if imported as a module into another script
    main()
