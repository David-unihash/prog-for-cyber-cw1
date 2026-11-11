#Security Event Logger
#used to get the current date and time
from datetime import datetime 
# used to generate a random event ID
import random 
#used to find the computer's IP address
import socket

#Correct username and password
correct_user = "admin"
correct_password = "admin123"

#Create a UDP socket(IPv4)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#this chooses the network the computer will use
s.connect(("8.8.8.8", 80))
#Read the computer's own IP from the socket
ip_address = s.getsockname()[0]
#Show the IP address on screen
print("IP Address:", ip_address)
#Close the socket now that we the IP address
s.close()

#Keep executing until the correct details are entered
while True:
    #Ask the user to type in logi details
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    #Recod the exact date and time of the login attempt 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #Give the login atempt a random ID number
    event_id = random.randint(1000, 9999)

    #Check if both username and password are correct 
    if user_name == correct_user and password == correct_password:
        print(f"Access granted. Welcome to the Security Event Logger." \
        f"\n Username: {user_name} " \
        f"\n Event ID: {event_id}" \
        f"\n IP Address: {ip_address}" \
        f"\n Event: Access Granted" \
        f"\n Timestamp: {timestamp}")
        #Stop the loop if the login is successful
        break
    else:
        #Wrong details the loop does not break it keeps asking 
        print(f"Access denied. Invalid credentials." \
        f"\n Username: {user_name} " \
        f"\n Event ID: {event_id}" \
        f"\n IP Address: {ip_address}" \
        f"\n Event: Access Denied" \
        f"\n Timestamp: {timestamp}")
