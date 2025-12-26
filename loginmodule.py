print("Welcome to CUBICROOM")
usernames=[]
passwords=[]
ans=input("Do you already have an account? y/n:")
if ans=="n":
    uid=input("Create a username:")
    password=input("create a password:")
    usernames.append(uid)
    print(f"Congratulations {uid.title()}, you have successfully created an account!!!")
elif ans=="y":
    uid=input("Enter your username:")
    for userid in usernames:
        if uid == userid:
            passcode=input("Enter your password:")
            for pw in passwords:
                if passcode==pw:
                    print("You have successfully logged in!")
                else:
                    print("You entered the wrong password")
        else:
            print("You have not crreated an account yet. Please create one.")
else:
    print("Please type 'y' for yes or 'n' for no.") 















