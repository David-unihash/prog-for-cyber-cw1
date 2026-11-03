#Security Event Counter

name = input("Enter your name or username: ")
print(f"Hi {name}, Pick a Securit tool.")

print("Below is a menu of some of the things you can do with this security tool")
print("Security Event Counter" \
"\nBrute-Force Simulation" \
"\nLogin Authentication" \
"\nExit")
option = input("Pick an option: ")

def security_event_counter():
    right_password = "Password123"
    r = 0
    w = 0
    for i in range(1, 11):
        password = input("Enter a password: ")
        if password == right_password:
            r += 1
        else:
            w += 1
    incorrect_percentage = w/10 * 100
    if incorrect_percentage > 50: 
        print(f"{incorrect_percentage}% of the passwords entered were incorrect")

def brute_force_simulator():
    correct_pass = "Secure123"
    for i in range(1,6):
        password = input("Enter the password: ")
        if password == correct_pass:
            break

def login_auth():
  right_user = "admin"
  right_password = "admin123"
  j = 0 
  for i in range(1,4):
      user = input("Enter a username: ")
      password = input("Enter a password: ")
      if user != right_user and password != right_password:
        j += 1
        print("Wrong username and password")
        if j == 3:
            print("Too many attempts, Account is frozen try again in 24 hours.")
      if user == right_user and password == right_password:
          print(f"Welcome {user}")
          break
          
def options():
    ans = input("Would you like to use another tool in the security tool? (y/n)")
    if ans == "y" or "Y":
        print("Security Event Counter" \
                "\nBrute-Force Simulation" \
                "\nLogin Authentication" \
                "\nExit")
    if ans == "n" or "N":
        print()

if option == "Security Event Counter":
    security_event_counter()
elif option == "Brute-Force Simulation":
    brute_force_simulator()
elif option == "Login Authentication":
    login_auth()
elif option == "Exit":
    print("Thank you for using the security tool.")
else:
    print("Not an option")