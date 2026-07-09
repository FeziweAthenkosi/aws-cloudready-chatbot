"""
=========================================================
Prompt Builder

This module builds prompts that are sent to Groq.

Each quiz type has its own prompt builder.
=========================================================
"""

from validators import (
    validate_quiz_type,
    validate_category,
    validate_service,
    validate_difficulty,
    validate_question_count
)

# =========================================================
# Shared JSON Output Schema
# =========================================================

JSON_OUTPUT_SCHEMA = """
Return ONLY valid JSON.

Do NOT use Markdown.

Do NOT wrap the JSON inside triple backticks.

Do NOT include any text before or after the JSON.

Use the following JSON structure exactly:

{
    "questions": [
        {
            "question": "Question text",

            "options": {
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            },

            "correct_answer": "A",

            "correct_explanation": "Explain why the correct answer is correct.",

            "incorrect_explanations": {
                "B": "Explain why B is incorrect.",
                "C": "Explain why C is incorrect.",
                "D": "Explain why D is incorrect."
            },

            "exam_tip": "Helpful AWS Cloud Practitioner exam tip."
        }
    ]
}
"""


# =========================================================
# Service Quiz Prompt
# =========================================================

def build_service_quiz_prompt(
    category,
    service,
    difficulty,
    question_count
):
    """
    Builds a prompt for an AWS Service Quiz.
    """

    system_prompt = """
You are an AWS Certified Cloud Practitioner exam writer.

Generate professional-quality AWS Cloud Practitioner
multiple-choice questions.

The questions should closely resemble the style,
difficulty and wording used in the real AWS certification exam.
"""

    context = f"""
Quiz Type:
Service Quiz

AWS Category:
{category}

AWS Service:
{service}

Difficulty:
{difficulty}

Number of Questions:
{question_count}
"""

    requirements = """
Requirements

1. Generate exactly the requested number of questions.

2. Every question must have exactly four options:
A)
B)
C)
D)

3. Only ONE option must be correct.

4. Questions must test understanding,
not simple memorization.

5. Questions should be clear,
professional and unambiguous.

6. Avoid duplicate questions.

7. Avoid repeating the same scenario.

8. Focus ONLY on the selected AWS service.

9. Ensure technical accuracy.

10. The difficulty must match the requested level.
"""

    explanations = """
For EVERY question include:

• Correct Answer

• Explanation of the correct answer

• Explanation for EACH incorrect option

• One AWS Cloud Practitioner Exam Tip
"""

    prompt = (
        system_prompt
        + context
        + requirements
        + explanations
        + JSON_OUTPUT_SCHEMA
    )

    return prompt


# =========================================================
# Category Quiz Prompt
# =========================================================

def build_category_quiz_prompt(
    category,
    difficulty,
    question_count
):
    """
    Build a prompt for a Category Quiz.
    """

    pass


# =========================================================
# Mock Exam Prompt
# =========================================================

def build_mock_exam_prompt(
    difficulty,
    question_count
):
    """
    Build a prompt for a Mock Exam.
    """

    pass


# =========================================================
# Main Prompt Router
# =========================================================

def build_prompt(
    quiz_type,
    category=None,
    service=None,
    difficulty="Easy",
    question_count=5
):
    """
    Validate inputs and route the request
    to the correct prompt builder.
    """

    # -------------------------
    # Common Validation
    # -------------------------

    validate_quiz_type(quiz_type)
    validate_difficulty(difficulty)
    validate_question_count(question_count)

    # -------------------------
    # Service Quiz
    # -------------------------

    if quiz_type == "Service Quiz":

        validate_category(category)
        validate_service(category, service)

        return build_service_quiz_prompt(
            category,
            service,
            difficulty,
            question_count
        )

    # -------------------------
    # Category Quiz
    # -------------------------

    elif quiz_type == "Category Quiz":

        validate_category(category)

        return build_category_quiz_prompt(
            category,
            difficulty,
            question_count
        )

    # -------------------------
    # Mock Exam
    # -------------------------

    elif quiz_type == "Mock Exam":

        return build_mock_exam_prompt(
            difficulty,
            question_count
        )

    # -------------------------
    # Unknown Quiz Type
    # -------------------------

    raise ValueError(
        f"Unknown quiz type: {quiz_type}"
    )