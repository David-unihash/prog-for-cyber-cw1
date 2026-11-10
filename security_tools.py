#Cyber Security Utilities 
# Random library was called  because it was needed for the random password function
import random

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        return "Password must contain at least one special character."
    
    return "Password is valid."

def validate_ip(ip):
    ip = ip.strip().split(".")

    if len(ip) != 4:
        return "Invalid IP address format."

    for addresses in ip:
        if not addresses.isdigit():
            return "Invalid IP address format."
        if not 0 <= int(addresses) <= 255:
            return "Invalid IP address range."
        if len(addresses) > 1 and addresses[0] == "0":
            return "Invalid IP address format."

    return "Valid IP address."

def generate_random_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    password_length = random.randint(8, 16)
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password
