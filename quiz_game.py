print("===================================")
print("      GENERAL KNOWLEDGE QUIZ")
print("===================================\n")

score = 0

# Question 1
print("1. What is the capital of India?")
print("A. Mumbai")
print("B. New Delhi")
print("C. Kolkata")
print("D. Chennai")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. New Delhi\n")

# Question 2
print("2. Which planet is known as the Red Planet?")
print("A. Venus")
print("B. Jupiter")
print("C. Mars")
print("D. Saturn")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. Mars\n")

# Question 3
print("3. How many continents are there in the world?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. 7\n")

print("===================================")
print("Quiz Completed!")
print("Your Final Score:", score, "/3")
print("===================================")