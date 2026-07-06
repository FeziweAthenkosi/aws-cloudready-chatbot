from prompts import build_prompt

prompt = build_prompt(
    quiz_type="Service Quiz",
    category="Compute",
    service="Amazon EC2",
    difficulty="Easy",
    question_count=5
)

print(prompt)