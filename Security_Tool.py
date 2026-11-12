#Security Event Counter

name = input("Enter your name or username: ") #Enter your name or username
print(f"Hi {name}, Pick a Securit tool.") #Prints the value you entered for name

#This is a list of the options below and you can choose from after entering your name
print("Below is a menu of some of the things you can do with this security tool")
print("Security Event Counter" \
"\nBrute-Force Simulation" \
"\nLogin Authentication" \
"\nExit")
option = input("Pick an option: ")

#This tool calculates the percentage of incorrectness of the passwords that were entered
def security_event_counter():
    right_password = "Password123"
    r = 0
    w = 0
    #This loop makes us enter a password up to ten times until we get the right password
    for i in range(1, 11):
        password = input("Enter a password: ")
        if password == right_password:
            r += 1
        else:
            w += 1
    incorrect_percentage = w/10 * 100
    #This checks that we passed 50% mark 
    if incorrect_percentage > 50: 
        print(f"{incorrect_percentage}% of the passwords entered were incorrect")

#This tool gives us a chance to write our password at least 5 times until we get the right password
def brute_force_simulator():
    correct_pass = "Secure123"
    
    #This loop gives you five attempts to enter a password
    for i in range(1,6):
        password = input("Enter the password: ")
        if password == correct_pass:
            break
            
#This tool checks that the login credentials are correct and lets us in if they are
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

#This function just makes sure we can select another tool in case we want to without ending the program and starting it up again
#This was just added by me for easier accessibility it wasn't needed
def options():
    ans = input("Would you like to use another tool in the security tool? (y/n): ")
    if ans == "y" or "Y":
       print("Security Event Counter" \
            "\nBrute-Force Simulation" \
            "\nLogin Authentication" \
            "\nExit")
        answer = input("Pick an answer: ")
        if answer == "Security Event Counter":
            security_event_counter()
        if answer == "Brute-Force Simulation":
            brute_force_simulator()
        if answer == "Login Authentication"
            login_auth()
    if ans == "n" or "N":
        print("Exit")
        #Call exit 

#This if and else block is for calling all the functions above they are chosen from the menu
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
