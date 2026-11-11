#import the file security_tools 
import security_tools
#import the functions from security_tools
from security_tools import validate_password
from security_tools import validate_ip
from security_tools import generate_random_password 


input_password = input("Enter your password: ")
validation_result = validate_password(input_password)
print(f"Password validation result: {validation_result}")

input_ip = input("Enter an IP address: ")
ip_validation_result = validate_ip(input_ip)
print(f"IP address validation result: {ip_validation_result}")

random_password = generate_random_password()
print(f"Generated random password: {random_password}")
