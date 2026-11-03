import random


print("\nSelect Difficulty!")
print("1: Easy (1~50)")
print("2: Normal (1~100)")

while True:
    choice = input("Enter difficulty (1 or 2): ").strip()
    if choice == "1":
        max_num = 50
        difficulty_name = "Easy"
        break
    elif choice == "2":
        max_num = 100
        difficulty_name = "Normal"
        break
    else:
        print("❌ Invalid input! Please enter '1' or '2'.")

target_number = random.randint(1, max_num)
attempts = 0

print(f"\n[{difficulty_name} Mode] Guess a number between 1 and {max_num}!")
print("Type 'q' anytime to quit.")

while True:
    user_input = input("Enter a number: ").strip()

    if user_input.lower() == "q":
        print("Exiting the game. Try again next time!")
        break

    try:
        guess = int(user_input)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number or 'q'.")
        continue

    attempts += 1

    if guess < target_number:
        print(" UP!")
    elif guess > target_number:
        print(" DOWN!")
    else:
        print(
            f"\nCorrect! [{difficulty_name} Mode] You found it in {attempts} attempts. Awesome!"
        )
        break


input("\nPress Enter to exit...")
