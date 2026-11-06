# IP Address Validator

def validate_ip(ip):
    ip = ip.strip().split(".")

    if len(ip) != 4:
        return False

    for addresses in ip:
        if not ip.isdigit():
            return False
        if not 0 <= int(ip) <= 255:
            return False
        if len(ip) > 1 and ip[0] == "0":
            return False

    return True

ip_address = input("Enter an IP address: ")
if validate_ip(ip_address):
    print(f"Valid {ip_address}")
else:
    print("Invalid")