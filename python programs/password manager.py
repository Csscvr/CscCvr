import json
import os

class PasswordManager:
    def __init__(self, filename):
        self.filename = filename
        self.passwords = self.load_passwords()

    def load_passwords(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_passwords(self):
        with open(self.filename, 'w') as f:
            json.dump(self.passwords, f)

    def add_password(self, account, password):
        self.passwords[account] = password
        self.save_passwords()
        print(f"Password added for {account}")

    def delete_password(self, account):
        if account in self.passwords:
            del self.passwords[account]
            self.save_passwords()
            print(f"Password deleted for {account}")
        else:
            print(f"No password found for {account}")

    def view_password(self, account):
        if account in self.passwords:
            print(f"Password for {account}: {self.passwords[account]}")
        else:
            print(f"No password found for {account}")

    def view_all_passwords(self):
        for account, password in self.passwords.items():
            print(f"Account: {account}, Password: {password}")


def main():
    # Specify the full path to the file where passwords will be saved
    filename = os.path.join(os.path.expanduser('~'), 'passwords.json')
    password_manager = PasswordManager(filename)

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add password")
        print("2. Delete password")
        print("3. View password")
        print("4. View all passwords")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            password_manager.add_password(account, password)
        elif choice == "2":
            account = input("Enter account name: ")
            password_manager.delete_password(account)
        elif choice == "3":
            account = input("Enter account name: ")
            password_manager.view_password(account)
        elif choice == "4":
            password_manager.view_all_passwords()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()