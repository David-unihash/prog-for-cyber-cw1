#import the file security_tools 
import security_tools
#import the functions from security_tools
from security_tools import validate_password
from security_tools import validate_ip
from security_tools import generate_random_password 

#This loop keeps asking until an appropriate password is entered
while True:
    password = input("Enter a password: ")
    result = validate_password(password)
    print(result)

    #if the right password is entered the loop breaks
    if result == "Password is valid.":
        break
#enter an ip address
input_ip = input("Enter an IP address: ")
#This calls the validate_ip function
ip_validation_result = validate_ip(input_ip)
print(f"IP address validation result: {ip_validation_result}")

#calls the generate_random_password function
random_password = generate_random_password()
print(f"Generated random password: {random_password}")
