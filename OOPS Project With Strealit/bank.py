from pathlib import Path
import json
import secrets
import string


class Bank:
    DATABASE = Path("data.json")

    def __init__(self):
        self.data = self._load_data()

    # -----------------------------
    # File Handling
    # -----------------------------

    def _load_data(self):
        try:
            if not self.DATABASE.exists():
                self.DATABASE.write_text("[]")
                return []

            with open(self.DATABASE, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                return []

        except (json.JSONDecodeError, OSError) as error:
            print(f"Error loading database: {error}")
            return []

    def _save_data(self):
        try:
            with open(self.DATABASE, "w") as file:
                json.dump(self.data, file, indent=4)

        except OSError as error:
            raise RuntimeError(f"Unable to save data: {error}")

    # -----------------------------
    # Account Number
    # -----------------------------

    def _generate_account_number(self):
        characters = (
            string.ascii_uppercase
            + string.digits
            + "!@#$%^&*"
        )

        while True:
            account_number = "".join(
                secrets.choice(characters)
                for _ in range(7)
            )

            if not self._find_by_account(account_number):
                return account_number

    # -----------------------------
    # Authentication
    # -----------------------------

    def _find_by_account(self, account_number):
        for user in self.data:
            if user["account_number"] == account_number:
                return user

        return None

    def authenticate(self, account_number, pin):
        user = self._find_by_account(account_number)

        if user and user["pin"] == pin:
            return user

        return None

    # -----------------------------
    # Create Account
    # -----------------------------

    def create_account(self, name, age, email, pin):

        name = name.strip()
        email = email.strip()

        if not name:
            return False, "Name cannot be empty."

        if age < 18:
            return False, "You must be at least 18 years old."

        if not self._validate_pin(pin):
            return False, "PIN must contain exactly 4 digits."

        # Prevent duplicate email
        for user in self.data:
            if user["email"].lower() == email.lower():
                return False, "An account with this email already exists."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_number": self._generate_account_number(),
            "balance": 0
        }

        self.data.append(account)
        self._save_data()

        return True, account

    # -----------------------------
    # PIN Validation
    # -----------------------------

    @staticmethod
    def _validate_pin(pin):
        pin = str(pin)

        return (
            len(pin) == 4
            and pin.isdigit()
        )

    # -----------------------------
    # Deposit
    # -----------------------------

    def deposit(self, account_number, pin, amount):

        user = self.authenticate(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "You can deposit a maximum of ₹10,000 at a time."

        user["balance"] += amount

        self._save_data()

        return True, user["balance"]

    # -----------------------------
    # Withdraw
    # -----------------------------

    def withdraw(self, account_number, pin, amount):

        user = self.authenticate(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount

        self._save_data()

        return True, user["balance"]

    # -----------------------------
    # Account Details
    # -----------------------------

    def get_account(self, account_number, pin):

        user = self.authenticate(account_number, pin)

        if not user:
            return None

        # Don't return PIN
        return {
            "name": user["name"],
            "age": user["age"],
            "email": user["email"],
            "account_number": user["account_number"],
            "balance": user["balance"]
        }

    # -----------------------------
    # Update Account
    # -----------------------------

    def update_account(
        self,
        account_number,
        pin,
        name=None,
        email=None,
        new_pin=None
    ):

        user = self.authenticate(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if name is not None and name.strip():
            user["name"] = name.strip()

        if email is not None and email.strip():
            user["email"] = email.strip()

        if new_pin is not None:

            if not self._validate_pin(new_pin):
                return False, "New PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        self._save_data()

        return True, "Account updated successfully."

    # -----------------------------
    # Delete Account
    # -----------------------------

    def delete_account(self, account_number, pin):

        user = self.authenticate(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        self.data.remove(user)

        self._save_data()

        return True, "Account deleted successfully."