
class ATM:
    def __init__(self, correct_pin='1234', balance=100.0, max_attempts=3):
        self.correct_pin = correct_pin
        self.balance = balance
        self.max_attempts = max_attempts
        self.attempts = 0
        self.authenticated = False

    def enter_pin(self, pin):
        if self.attempts >= self.max_attempts:
            print("PIN entry limit exceeded. Access rejected.")
            return "Rejected"
        if pin == self.correct_pin:
            print("PIN correct. Authentication successful.")
            self.authenticated = True
            return "Authenticated"
        else:
            self.attempts += 1
            print(f"Incorrect PIN. Attempt {self.attempts} of {self.max_attempts}.")
            if self.attempts >= self.max_attempts:
                print("Too many incorrect attempts. Access rejected.")
                return "Rejected"
            return "Retry"

    def check_balance(self):
        if self.balance <= 0:
            print("Account balance is zero. Account closed.")
            return "Closed"
        else:
            print(f"Account balance is ${self.balance:.2f}")
            return "Sufficient"

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        print(f"${amount:.2f} withdrawn. Remaining balance: ${self.balance:.2f}")
        return True

# Simulation scenarios
atm = ATM(balance=100.0)

print("\n--- Scenario: Correct PIN and Withdrawal ---")
state = atm.enter_pin("1234")
if state == "Authenticated":
    if atm.check_balance() == "Sufficient":
        atm.withdraw(50)

print("\n--- Scenario: Incorrect PIN x3 ---")
atm2 = ATM()
atm2.enter_pin("0000")
atm2.enter_pin("1111")
atm2.enter_pin("2222")

print("\n--- Scenario: Correct PIN but Zero Balance ---")
atm3 = ATM(balance=0)
state = atm3.enter_pin("1234")
if state == "Authenticated":
    atm3.check_balance()
