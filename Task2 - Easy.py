
quiz = [
    {
        "question": "1) Which of the following is not a programming language?",
        "options": ["a) Python", "b) Java", "c) HTML", "d) C++"],
        "answer": "c"
    },
    {
        "question": "2) What does HTML stand for?",
        "options": [
            "a) Hyper Text Markup Language",
            "b) High Transfer Markup Language",
            "c) Hyperlink Text Management Language",
            "d) Hyper Tool Multi Language"],
        "answer": "a"
    },
    {
        "question": "3) In Python, what symbol is used for comments?",
        "options": ["a) //", "b) #", "c) /* */", "d) <!-- -->"],
        "answer": "b"
    },
    {
        "question": "4) Which company developed the Windows operating system?",
        "options": ["a) Apple", "b) Microsoft", "c) IBM", "d) Google"],
        "answer": "b"
    },
    {
        "question": "5) What does 'CPU' stand for?",
        "options": [
            "a) Central Process Unit",
            "b) Central Processing Unit",
            "c) Control Processing Utility",
            "d) Central Performance Unit"],
        "answer": "b"
    }
]

score = 0
print("Welcome to the IT Quiz!\n")

for q in quiz: #Prints out the questions and its options
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (a/b/c/d): ").lower() #Lowers the input by user
    
    if user_answer == q["answer"]:
        print("Correct!\n") # Conditional statement for input check
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print(f"Quiz Over! You scored {score} out of {len(quiz)}.")
