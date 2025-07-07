# week3_submission_Ishan_Bhartiya

Package : kratos_new_q1

Path of node: kratos_Ishan_Bhartiya/kratos_new_q1/kratos_new_q1/Q1_Publisher.py
 
This file belongs to Question 1 and is responsible for publishing 'Hello' over the topic called 'new' at a rate of 15Hz

Path of node: kratos_Ishan_Bhartiya/kratos_new_q1/kratos_new_q1/Q1_Subscriber.py

This file belongs to Question 1 and is subscribed to the topic 'new', it
receives the message 'Hello', and prints it at a rate of 15Hz to the console

-------------------------------------------------------------------------------------------------

Package : kratos_new_q2

Path of node: kratos_Ishan_Bhartiya/kratos_new_q2/kratos_new_q2/Q2_Publisher.py

This file belongs to Question 2 and is responsible for publishing 'Red' or 'Green' to the topic 's1' alternately at a rate of 0.1Hz

Path of node: kratos_Ishan_Bhartiya/kratos_new_q2/kratos_new_q2/Q2_Subscriber.py

This file belongs to Question 2 and is subscribed to the topic 's1', if the received message is 'Red', it instantly publishes 'Green' and vice versa to the topic 's2'

-------------------------------------------------------------------------------------------------

Package : kratos_new_1

Path of node: kratos_Ishan_Bhartiya/kratos_new_1/kratos_new_1/Q3.py

This file belongs to Question 3 and is responsible for publishing a custom message to the topic 'Rover_Comm' at a rate of 0.1Hz

Path of msg file : kratos_Ishan_Bhartiya/kratos_new_1/msg

This is an msg file which contains the custom message to be sent across the topic Rover_Comm, it contains integer, float, 3-D vectors describing linear and angular velocities, and a 2-D position message types

-------------------------------------------------------------------------------------------------

Package : kratos_new_q4

Path of node : kratos_Ishan_Bhartiya/kratos_new_q4/kratos_new_q4/Q4_Publisher.py

This file belongs to Question 4 and is responsible for publishing on 4 different topics, 'second', 'minute', 'hour' and 'clock', at a rate of 1Hz. As their names suggest, the messages being published are time parameters, namely seconds, minutes, hours, and lastly time is published as a string with the format Hours:Minutes:Seconds

-------------------------------------------------------------------------------------------------
