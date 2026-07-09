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

Your task is to generate high-quality AWS Cloud Practitioner
multiple-choice questions.
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
Requirements:

1. Generate the requested number of questions.

2. Every question must have exactly four options:
A)
B)
C)
D)

3. Only one option must be correct.

4. The questions should resemble the style of the
AWS Certified Cloud Practitioner exam.

5. Avoid ambiguous wording.

6. Do not repeat questions.
"""

    explanations = """
For every question provide:

• Correct Answer

• Explanation of why the correct answer is correct.

• Explanation of why EACH incorrect option is incorrect.

• One AWS Cloud Practitioner Exam Tip.
"""

    output_format = """
Return the response as valid JSON.

Do not use Markdown.

Do not include any additional commentary outside the JSON.
"""

    prompt = (
        system_prompt
        + context
        + requirements
        + explanations
        + output_format
    )

    return prompt


def build_category_quiz_prompt(
    category,
    difficulty,
    question_count
):
    """
    Build a prompt for a Category Quiz.
    """
    pass


def build_mock_exam_prompt(
    difficulty,
    question_count
):
    """
    Build a prompt for a Mock Exam.
    """
    pass

def build_prompt(
    quiz_type,
    category=None,
    service=None,
    difficulty="Easy",
    question_count=5
):
    """
    Validate the request and route it
    to the appropriate prompt builder.
    """

    # Validate inputs common to all quiz types
    validate_quiz_type(quiz_type)
    validate_difficulty(difficulty)
    validate_question_count(question_count)

    # Service Quiz
    if quiz_type == "Service Quiz":

        validate_category(category)
        validate_service(category, service)

        return build_service_quiz_prompt(
            category,
            service,
            difficulty,
            question_count
        )

    # Category Quiz
    elif quiz_type == "Category Quiz":

        validate_category(category)

        return build_category_quiz_prompt(
            category,
            difficulty,
            question_count
        )

    # Mock Exam
    elif quiz_type == "Mock Exam":

        return build_mock_exam_prompt(
            difficulty,
            question_count
        )

    else:
        raise ValueError(f"Unknown quiz type: {quiz_type}")
