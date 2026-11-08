#Security Event Logger
from datetime import datetime
import random
import socket

correct_user = "admin"
correct_password = "admin123"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.connect(("8.8.8.8", 80)) 
ip_address = s.getsockname()[0] 
print("IP Address:", ip_address) 
s.close()

while True:
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event_id = random.randint(1000, 9999)

    if user_name == correct_user and password == correct_password:
        print(f"Access granted. Welcome to the Security Event Logger." \
        f"\n Username: {user_name} " \
        f"\n Event ID: {event_id}" \
        f"\n IP Address: {ip_address}" \
        f"\n Event: Access Granted" \
        f"\n Timestamp: {timestamp}")
        break
    else:
        print(f"Access denied. Invalid credentials." \
        f"\n Username: {user_name} " \
        f"\n Event ID: {event_id}" \
        f"\n IP Address: {ip_address}" \
        f"\n Event: Access Denied" \
        f"\n Timestamp: {timestamp}")
