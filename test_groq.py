from prompts import build_prompt
from groq_client import generate_response
from parser import parse_quiz_response


prompt = build_prompt(
    quiz_type="Service Quiz",
    category="Compute",
    service="Amazon EC2",
    difficulty="Easy",
    question_count=1
)

print("Sending request to Groq...\n")

response = generate_response(prompt)

quiz = parse_quiz_response(response)

for i, question in enumerate(quiz["questions"], start=1):
    print(f"\nQuestion {i}")
    print("-" * 50)

    print(question["question"])
    print()

    for option, text in question["options"].items():
        print(f"{option}. {text}")

    print()
    print("Correct Answer:", question["correct_answer"])
    print()
    print("Explanation:")
    print(question["correct_explanation"])
    print()
    print("Exam Tip:")
    print(question["exam_tip"])