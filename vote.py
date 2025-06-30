from users import User

class votingSystem:
    Parties = {"PTI": 0, "TLP": 0, "Pak army": 0, "PML(n)": 0}
    
    def vote(self):
        username = input("Enter your Username: ")
        Password = input("Enter your Password: ")
        user = User.authenticate(username, Password)
        if user:
            if user.voted:
                print("\nUser already cast their vote.")
                return
            print("\nParties PTI, TLP, PAk army, PML(n)\n")
            choice = input("\nSelect your suggestion: ").upper()
            if choice in self.Parties:
                self.Parties[choice] += 1
                user.voted = True
                print("\nVote cast successfully.\n")
            else:
                print("Invalid selection.")
        else:
            print("Invalid Username or Password")

    def Results(self):
        print("\nVoting Result:\n")
        for party, votes in self.Parties.items():
            print(f"Party {party} = {votes} Votes.\n")
