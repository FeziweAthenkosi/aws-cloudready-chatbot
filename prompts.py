"""
=========================================================
Prompt Builder

This module builds prompts that are sent to Groq.

Each quiz type has its own prompt builder.
=========================================================
"""
from config import *

def build_service_quiz_prompt(
    category,
    service,
    difficulty,
    question_count
):
    """
    Build a prompt for a Service Quiz.
    """
    pass


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
    Routes the request to the correct prompt builder.
    """

    if quiz_type == "Service Quiz":
        return build_service_quiz_prompt(
            category,
            service,
            difficulty,
            question_count
        )

    elif quiz_type == "Category Quiz":
        return build_category_quiz_prompt(
            category,
            difficulty,
            question_count
        )

    elif quiz_type == "Mock Exam":
        return build_mock_exam_prompt(
            difficulty,
            question_count
        )

    else:
        raise ValueError(f"Unknown quiz type: {quiz_type}")
    
from config import (
    CHATBOT_NAME,
    CERTIFICATION
)

print(CHATBOT_NAME)
print(CERTIFICATION)