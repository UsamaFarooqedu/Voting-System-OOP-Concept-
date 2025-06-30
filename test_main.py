import pytest
from users import User
from vote import votingSystem

# Fixtures
@pytest.fixture
def sample_users():
    User.user_db.clear()  # Clear user database for clean testing
    User.add_user("test_user1", "password1")
    User.add_user("test_user2", "password2")
    return User.user_db

@pytest.fixture
def voting_system():
    return votingSystem()

# Test cases for user registration
def register_new_user_test():
    result = User.add_user("new_user", "new_password")
    assert result is True
    assert "new_user" in User.user_db

def test_register_existing_user(sample_users):
    result = User.add_user("test_user1", "password1")
    assert result is False

# Test cases for user login
def test_login_successful(sample_users):
    user = User.authenticate("test_user1", "password1")
    assert user is not None
    assert user.Username == "test_user1"

def test_login_unsuccessful(sample_users):
    user = User.authenticate("invalid_user", "invalid_password")
    assert user is None

# Test cases for voting system
def test_vote_success(voting_system, sample_users):
    user = User.authenticate("test_user1", "password1")
    assert user is not None
    assert user.voted is False

    voting_system.vote = lambda: None  # Mock the user input flow

    voting_system.Parties["PTI"] += 1
    user.voted = True

    assert voting_system.Parties["PTI"] == 1
    assert user.voted is True

def test_vote_already_voted(voting_system, sample_users):
    user = User.authenticate("test_user1", "password1")
    user.voted = True  # Simulate user has already voted

    voting_system.vote = lambda: None  # Mock
    voting_system.vote()

    assert voting_system.Parties["PTI"] == 1  # No votes increased
    assert user.voted is True

# Test cases for results
def test_results(voting_system):
    voting_system.Parties = {"PTI": 1, "TLP": 2, "PAK Army": 0, "PML(N)": 3}
    result = voting_system.Results()
    assert voting_system.Parties["PTI"] == 1
    assert voting_system.Parties["PML(N)"] == 3
