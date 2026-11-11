#Cyber Security Utilities 
# Random library was called because it was needed for the random password function
import random

#This function is used to check that password meets certain conditions 
def validate_password(password):
    special_char = "!@#$%^&*()_-=+[]{}|;:;\",.<>?/`~"

    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    # Go through the password one character at a time
    for char in password:
        #checks if a character is a digit
        if char.isdigit():
            has_digit = True
        #checks if there are uppercase values in the password
        elif char.isupper():
            has_upper = True
        #checks if there are lowercase values in the password
        elif char.islower():
            has_lower = True
        #checks if there are special charcters in the passsword
        elif char in special_chars:
            has_special = True

    # Now check each rule
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_special:
        return "Password must contain at least one special character."

    return "Password is valid."

#This function checks to validate an ip address
def validate_ip(ip):
    #Remove any space at the start or end, and split the text at each dot
    ip = ip.strip().split(".")
    
    #Checks the address for four parts
    if len(ip) != 4:
        return "Invalid IP address format."
        
    #Check each part one at a time
    for addresses in ip:
        #Each part must be made up of digits only
        if not addresses.isdigit():
            return "Invalid IP address format."
            
        #Each number must be between 0 and 255
        if not 0 <= int(addresses) <= 255:
            return "Invalid IP address range."

        #This checks that it can 't start with "0"
        if len(addresses) > 1 and addresses[0] == "0":
            return "Invalid IP address format."

    #If it passes all the above the IP is valid
    return "Valid IP address."

#This generates a new random password 
def generate_random_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    #pick a random length between 10 and 16
    password_length = random.randint(10, 16)

    #Start with an empty password and build it
    password = ""

    #Loop through for every character the password needs
    for i in range(password_length):
        #Pick one random character from the list and add it to the end
        password += random.choice(characters)

    #Return the password 
    return password
