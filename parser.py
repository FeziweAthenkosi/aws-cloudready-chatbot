"""
=========================================================
JSON Parser

Parses the JSON returned by Groq.
=========================================================
"""

import json


def parse_quiz_response(response):
    """
    Converts the Groq JSON response into
    a Python dictionary.
    """

    try:

        quiz = json.loads(response)

        return quiz

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Invalid JSON received from Groq.\n{e}"
        )