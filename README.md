
📊 Voting System (OOP-Based Python Project)

A secure, modular, and tested voting system built using Object-Oriented Programming (OOP) principles in Python. 
This project simulates a real-world voting process where users can register, authenticate, cast votes, 
and view results while ensuring data integrity and preventing fraud (e.g., duplicate votes).

🔍 Project Overview

🎯 Key Features
    ✔ User Management – Register and log in securely.
    
    ✔ Voting Mechanism – Users can vote for predefined political parties.
    
    ✔ Anti-Fraud Protection – Prevents users from voting multiple times.
    
    ✔ Real-Time Results – Displays live vote counts for each party.
    
    ✔ Unit Testing – Includes pytest test cases for reliability.

⚙️ How It Works

  User Registration → Users create an account with a username & password.
  
  Login → Only registered users can access the voting system.
  
  Voting → Users select a party, and their vote is recorded.
  
  Results → Admins or users can check the current vote distribution.

📂 Project Structure & Code Explanation

1. users.py – User Authentication System
    User Class: Manages user data (username, password, voting status).
    
    user_db (Dictionary): Stores all registered users.
    
    add_user(): Adds a new user (checks for duplicates).
    
    authenticate(): Verifies login credentials.
    
    Register() & login() Functions: Handle CLI-based user input.

2. vote.py – Voting Logic
    VotingSystem Class: Manages votes and results.
    
    Parties (Dictionary): Tracks vote counts for each party.
    
    vote(): Authenticates users, prevents duplicate votes, and records votes.
    
    Results(): Displays the current vote count.

3. main.py – CLI Interface
    Provides a menu-driven interface with options:
    
    Register → Create a new account.
    
    Login → Access the voting system.
    
    Vote → Cast a vote (if authenticated).
    
    View Results → Check election status.
    
    Exit → Close the program.

4. test_main.py – Unit Testing
    Uses pytest to verify:
    
    ✅ User registration & login.
    
    ✅ Voting functionality (success & fraud prevention).
    
    ✅ Result calculation.

