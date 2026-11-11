# IP Address Validator

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
