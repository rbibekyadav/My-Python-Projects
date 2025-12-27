print("Welcome to Cubic Room")
usernames=[]
passwords=[]
while True:
    ans=input("Do you already have an account?: y/n")
    if ans == "y":
        username=input("Enter your username:")
        if username in usernames:
            password=input("Enter your password:")
            if password in passwords:
                print("You have successfully Logged in!!!")
            else:
                print("You have entered a wrong password. Please try again.")    
        else:
            print("Username not found. Please create an account.")
    elif ans == "n":
        username=input("Create a username:")
        usernames.append(username)
        password=input("Create a password:")
        passwords.append(password)
        print("please login with the username and password that you have created just now.")
    else:
        print("Please enter 'y' for yes and 'n' for no.")   




           
            












