import hashlib

def create_password_hash(password):
    # Generate a salt (random value) to add to the password
    salt = "somerandomsalt"

    # Combine the password and salt
    salted_password = password + salt

    # Hash the salted password using a hashing algorithm (e.g., SHA256)
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    return hashed_password

def authenticate(password, hashed_password):
    # Create a hash of the provided password
    input_hashed_password = create_password_hash(password)

    # Compare the input hashed password with the stored hashed password
    if input_hashed_password == hashed_password:
        return True
    else:
        return False

# Example usage
stored_hashed_password = create_password_hash("mypassword")

# Authenticate a user
password_attempt = input("Enter your password: ")
if authenticate(password_attempt, stored_hashed_password):
    print("Authentication successful!")
else:
    print("Authentication failed.")
