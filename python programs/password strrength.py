import re

def password_strength(password):
    strength = 0

    # Check password length
    if len(password) < 8:
        return "Weak"

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    if strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"

def main():
    while True:
        password = input("Enter a password (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        if not password:
            print("Please enter a password.")
            continue
        try:
            print("Password strength:", password_strength(password))
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()