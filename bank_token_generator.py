#a code to generate tokens usable in banks
import sys, random, time
cd = ao = la = cbi = csi = 100
def cash_deposit():
    global cd
    print("Your token number for cash deposit is "+"'CD" +str(cd)+"'\n" )
    cd = cd + 1

def account_opening():
    global ao
    print("Your token number for account opening is "+"'AO" +str(ao)+"'\n")
    ao = ao + 1

def loan_applications():
    global la
    print("Your token number for cash deposit is "+"'LA" +str(la)+"'\n")
    la = la + 1

def check_book_issuance():
    global cbi
    print("Your token number for checkbook issuance is "+"'CBI" +str(cbi)+"'\n")
    cbi = cbi + 1

def customer_service_inquiry():
    global csi
    print("Your token number for customer service inquiry is "+"'CSI" +str(csi)+"'\n")
    csi = csi + 1

def reset_all_tokens():
    cd = ao = la = csi = cbi = 100
    print("\n\nALL TOKENS RESET/n/n")

print("Welcome to Siddharth Bank Ltd.")
print("How can we help you?")
options = True
while options:
    print("1.Cash Deposit\n2.Account Opening\n3.Loan Applications\n4.Check Book Issuance\n5.Customer Service Inquiries\n6.Reset all token.\n7.EXIT the program.")
    error = True
    while error:
        try:
            user_input = int(input("Enter the respective number for your purpose: "))
            if  int(user_input) <= 7 and int(user_input) >= 1 :
                error = False
            else:
                print("Input a valid number: ")
                error = True
        except ValueError:
            print("Please enter a valid number.")

    if user_input == 1:
        cash_deposit()
    elif user_input == 2:
        account_opening()
    elif user_input == 3:
        loan_applications()
    elif user_input == 4:
        check_book_issuance()
    elif user_input == 5:
        customer_service_inquiry()
    elif user_input == 6:
        reset_all_tokens()
    elif user_input == 7:
        print("Thanks for banking with us. \n---Have a Nice Day---")
        time.sleep(1)
        sys.exit()


