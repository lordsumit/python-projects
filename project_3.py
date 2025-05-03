import random

# Define the question generator
def generate_question():
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    elif operator == '*':
        answer = n1 * n2
    elif operator == '/':
        # Ensure division is clean and no divide by zero
        while n2 == 0 or n1 % n2 != 0:
            n1 = random.randint(1, 100)
            n2 = random.randint(1, 100)
        answer = n1 // n2  # Use integer division
        operator = '//'    # Show correct operator used in output

    return f"{n1} {operator} {n2}", answer

# Main game loop
def math_quiz():
    score = 0
    rounds = 10
    print("\n---- Welcome to the Math Quiz Game! ----")
    print("You will be given 10 math questions. Enter the correct number.\n")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\n----- Game Over! -----")
    print(f"Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Congrats! Tum hero ho! 🏆")
    elif score >= rounds // 2:
        print("Thik hi h bhai, padhai kar 😅")
    else:
        print("Chhor de padhai... 🤦")

math_quiz()
