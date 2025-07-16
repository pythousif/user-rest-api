# ── mini‑operations ────────────────────────────────────────────────────────────
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# ── helper for safe numeric input ──────────────────────────────────────────────
def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("❌  Please enter a valid number.\n")


# ── main program loop ──────────────────────────────────────────────────────────
def main() -> None:
    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (−)", subtract),
        "3": ("Multiplication (×)", multiply),
        "4": ("Division (÷)", divide),
        "q": ("Quit", None),
    }

    print("🖩  Simple CLI Calculator\n")

    while True:
        # Show menu
        for key, (label, _) in operations.items():
            print(f"{key.rjust(2)}) {label}")
        choice = input("\nSelect an option: ").lower().strip()

        if choice == "q":
            print("\nGoodbye!")
            break

        if choice not in operations:
            print("❌  Invalid selection.\n")
            continue

        # Get operands and compute result
        num1 = read_number("First number  : ")
        num2 = read_number("Second number : ")

        try:
            result = operations[choice][1](num1, num2)   # call the chosen function
            print(f"Result → {result}\n")
        except ZeroDivisionError as err:
            print(f"❌  {err}\n")


# ── script entry point ────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
