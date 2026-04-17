"""
Mini Project: Simple Console Calculator (Beginner Friendly)

Features:
-- Class based Calculator
-- Basic operations
-- Loop for repeated use
-- History stored in a list
-- Save and load history using a text file
-- Simple error handling
"""

HISTORY_FILE = "calc_history.txt"

class Calculator:

    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        data = []
        try:
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data.append(line)
        except FileNotFoundError:
            pass
        return data

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            for item in self.history:
                f.write(item + "\n")

    def get_number(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError:
                print("Enter a valid number")

    def add(self, a, b):
        return a + b
     
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
        
    def calculate(self, choice):
        a = self.get_number(message = "Enter first number: ")
        b = self.get_number(message = "Enter second number: ")
     
        if choice == "1":
            result = self.add(a, b)
            op = "+"
        elif choice == "2":
            result = self.subtract(a, b)
            op = "-"
        elif choice == "3":
            result = self.multiply(a, b)
            op = "*"
        elif choice == "4":
            result = self.divide(a, b)
            op = "/"
        else:
            return
        
        if result is not None:
            record = f"{a} {op} {b} = {result}" 
            print("Result: ", result)
            self.history.append(record)
    
    def show_history(self):
        if not self.history:
            print("No calculations yet.")
            return
        print("\nPrevious Calculations: ")
        for item in self.history:
            print(item)

def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show history")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            calc.calculate(choice)
        elif choice == "5":
            calc.show_history()
        elif choice == "6":
            calc.save_history()
            print("Goodbye. History Saved.")
            break
        else:
            print("Invalid choice. Try again.")
        
if __name__ == "__main__":
    main()


    
    
