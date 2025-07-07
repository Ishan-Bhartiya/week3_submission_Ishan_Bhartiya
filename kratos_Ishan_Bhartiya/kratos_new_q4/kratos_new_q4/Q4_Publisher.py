#!/usr/bin/python3 #Shebang for python files
#Importing necessary modules and libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Publisher')#Naming the node as Publisher
        self.publisher_1 = self.create_publisher(Int32,'second',10) #Creates publisher object, Publishes Int32 type object to the topic called 'second'
        self.publisher_2 = self.create_publisher(Int32,'minute',10)#Creates publisher object, Publishes Int32 type object to the topic called 'minute'
        self.publisher_3 = self.create_publisher(Int32,'hour',10)#Creates publisher object, Publishes Int32 type object to the topic called 'hour'
        self.publisher_4 = self.create_publisher(String,'clock',10)#Creates publisher object, Publishes String type object to the topic called 'clock'
        
        self.timer = self.create_timer(1,self.timer_callback)#Calls the function timer_callback every 1 second
        self.s=0
        self.m=0
        self.h=0
        
    def timer_callback(self):
        '''Creates objects of Int32(Integer) or String() data types'''
        second=Int32()
        minute=Int32()
        hour=Int32()
        time=String()

        '''Assigning the data fields of the messages to the respective instance variables'''
        second.data = self.s 
        minute.data = self.m
        hour.data = self.h
        time.data = str(hour.data)+":"+str(minute.data)+":"+str(second.data)#All the integer type data are converted to strings and concatenated in this fashion to get the required Hours:Minutes:Seconds
        
        '''Initially second.data,miniute.data and hour.data hold the value 0, seconds gets incremented every seconds, when it hits 60, its value is set to 0 and minute is incremented by 1
        when minute hits 60, its value is set to 0 and hour is incremented by 1 '''
        self.s=self.s+1
        if self.s==60:
            self.s=0
            self.m+=1
            if self.m==60:
                self.m=0
                self.h+=1
        
        
        self.publisher_1.publish(second)#Publishes the message called second
        self.publisher_2.publish(minute)#Publishes the message called minute
        self.publisher_3.publish(hour)#Publishes the message called hour
        self.publisher_4.publish(time)#Publishes the message called time
        print(time.data) #Prints 'time' to the console
        
def main(args=None):
    rclpy.init(args=args)#Initialises the rclpy python library
    minimal_publisher=MinimalPublisher()#Creates an instance of the MinimalSubscriber class
    rclpy.spin(minimal_publisher)#Keeps running the above created class till stopped


if __name__ == '__main__':#Sets __name__ to '__name__' if called directly to be run, this doesn't happen if it is called as a module in another script
    main() #Doing this makes sure that it doesn't run if the file is called into another script to act as a module
