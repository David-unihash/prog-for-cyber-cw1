#Security Incdent Manager

#Display the user informationa and event details in a structured format
user_info = {
    "user_name": "David",
    "ip_address": "192.168.10.1",
    "event_type": "Break in Attempt",
    "risk_level": "High",
}

#Display the user information and event details
print("Username: ", user_info["user_name"])
print("IP Address: ", user_info["ip_address"])
user_info["status"] = "Inactive"
user_info["risk_level"] = "medium"
# Display the updated user information and the remaining details
print("Event: ", user_info["event_type"])
print("Risk Level: ", user_info["risk_level"])
print("Status: ", user_info["status"])
