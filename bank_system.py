class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        # TO COMPLETE
        print(self.first_name)
        print(self.last_name)
        print(self.gender)
        print(self.street_address)
        print(self.city)
        print(self.city)
        print(self.email)
        print(self.cc_number)
        print(self.cc_type)
        print(self.balance)
        print(self.account_no)


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])

def findUser():
    # TO COMPLETE
    user_to_find_first_name = input("what's your first name: ").title()
    user_to_find_last_name = input('what is your last name').title()
    for user in userList:
        if user.first_name and user.last_name == user_to_find_first_name and user_to_find_last_name:
            print(f"{user.first_name} and {user.last_name}")
            return user
        else:
            print('sorry no user with tthat name found')
            return None





def overdrafts():
    # TO COMPLETE
    number_of_overdrafts = 0
    total_amount_overdrafts = 0
    for user in userList:
        if user.balance < 0:
            number_of_overdrafts += 1
            total_amount_overdrafts += sum(user.balance)
            print(user.first_name and user.last_name)
    print(f'TThe tottal number of overdrafts are {number_of_overdrafts}')
    print(f'the ttottal amount are {total_amount_overdrafts}')

def missingEmails():
    # TO COMPLETE
    missingEmails_number = 0
    for user in userList:
        if not user.email:
            missingEmails_number += 1
            print(f"{user.first_name} {user.last_name}")
            print(f"the total number of missing emails are {missingEmails_number}")

    True

def bankDetails():
    # TO COMPLETE
    total_number_users = 0
    Bank_worth = 0
    for user in userList:
        total_number_users += 1
        Bank_worth += user.balance
        print(f"There are {total_number_users} users")
        print(f"The total worth is {Bank_worth}")
        minium_balance = min(user.balance)
        print(f"{minium_balance}")
        max_balance = userList[8]
        print(f"{max_balance}")




def transfer():
    # TO COMPLETE
    account_number = input("what's your account number: ")
    for user in userList:
        if user.account_no == account_number:
            print(user.first_name and user.last_name)
            print(user.balance)
            amount_to_transfer = input("what's the amount you want transfer: ")
            if amount_to_transfer < user.balance:
                account_to_transfer = input("what the account number you want to transfer: ")
                print(user.first_name and user.last_name)
                confirm = input(f"Do you want to transfer {amount_to_transfer} to {account_to_transfer}?:"
                                f"Press Y to agree and N to cancel").title()
                #if confirm == "Yes":


            else:
                print("sorry that amount is over than the balance you have"
                      "in your current account")


    True

userList = []
generateUsers()


userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()
