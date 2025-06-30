from users import User,Register, login
from vote import votingSystem


def main():

    voting = votingSystem()
    print("\n=== Voting System ===\n")
    while True:
        print("Select (1) For Register")
        print("Select (2) For Login")
        print("Select (3) For Vote")
        print("Select (4) To View Result")
        print("Select (5) For Exit\n")
        choice = input("Enter your Choice: ")
        if (choice =="1"):
            Register()
        elif (choice =="2"):
            login()
        elif (choice =="3"):
            voting.vote()
        elif (choice =="4"):
            voting.Results()
        elif (choice =="5"):
            print("Exit the System.")
            break
        else:
            print("\nInvalid Choice; Please try again\n")






if __name__=="__main__":
    main()




