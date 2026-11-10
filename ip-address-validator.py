# IP Address Validator

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
