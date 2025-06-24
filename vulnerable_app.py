import os
import subprocess
import hashlib

# Insecurely using subprocess.call with user input - SAST should flag this
def run_command_insecurely():
    user_input = input("Enter a command to run: ")
    # This is vulnerable to command injection
    subprocess.call("ping " + user_input, shell=True) # BAD: shell=True with user input

# Insecure use of hashlib.md5 for passwords - SAST might flag this for weak hashing context
def hash_password_weakly(password):
    # BAD: MD5 is not suitable for password hashing
    return hashlib.md5(password.encode()).hexdigest()

# Hardcoded password - SAST should flag this
HARDCODED_SECRET = "my_super_secret_password_123" # BAD: Hardcoded secret

def main():
    print("--- Vulnerable App ---")
    run_command_insecurely()
    hashed_pw = hash_password_weakly("user_password")
    print(f"Weakly hashed password: {hashed_pw}")
    print(f"Hardcoded secret: {HARDCODED_SECRET}")
    print("--- End App ---")

if __name__ == "__main__":
    main()
