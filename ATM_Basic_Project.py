#ATM CODE:
user_name="Gunnam Pravallika"
user_pin=1234
Balance=200000
# pin=int(input("Please enter your 4 digit pin:"))
# if pin==user_pin:
while(True):
    print("welcome to your bank account "+user_name)
    print(" 1.Logout and Exit")
    print(" 2.View Account Balance")
    print(" 3.Withdraw Cash")
    print(" 4.Deposit Cash")
    print(" 5.Change PIN")
    option=int(input("please select number to proceed>"))
    if option==1:
        print("Existing....")
        print("you have been Logged out....,Thank You!")
    
    elif option==2:
        pin=int(input("Please enter your 4 digit pin>"))
        if pin==user_pin:
            print("Account Authorized!")
            print("Loading Account Balance")
            print("Your current Balance is:",Balance)
    
    elif option==3:
        pin=int(input("Please enter your 4 digit pin>"))
        if pin==user_pin:
            print("your account is authorized!....") 
            w=int(input("please enter the amount you wish to withdraw>"))
            if w>Balance:
                print("can't with draw RS.",w)
                print("enter the lower amount!")
            else:
                print("Withdrawn Amount>",w)
                print("Available Balance>",Balance-w)
                print("Thank You!")

    elif option==4:
        pin=int(input("Please enter your 4 digit pin>"))
        if pin==user_pin:
            print("your account is authorized!....")
            d=int(input("please enter the amount you wish to deposit>"))
            print("Amount deposited",d)
            print("Updated Balance:",Balance+d)

    elif option==5:
        pin=int(input("Please enter your 4 digit pin>"))
        if pin==user_pin:
            pc=int(input("please enter your new pin>"))
            print("your PIN Changed..,THANK YOU!)")
else:
    print("INCORRECT PIN")
