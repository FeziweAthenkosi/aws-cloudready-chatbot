import config


def validate_quiz_type(quiz_type):
    """
    Validate the selected quiz type.
    """

    if quiz_type not in config.QUIZ_TYPES:
        raise ValueError(
            f"Invalid quiz type: {quiz_type}"
        )

    return True

def validate_category(category):
    """
    Validate the selected AWS category.
    """

    if category not in config.AWS_CATEGORIES:
        raise ValueError(
            f"Invalid AWS category: {category}"
        )

    return True

def validate_service(category, service):
    """
    Validate that the selected AWS service belongs
    to the selected AWS category.
    """

    # Make sure the category exists first.
    validate_category(category)

    if service not in config.AWS_CATEGORIES[category]:
        raise ValueError(
            f"{service} is not a valid service in the {category} category."
        )

    return True

def validate_difficulty(difficulty):
    """
    Validate the selected difficulty level.
    """

    if difficulty not in config.DIFFICULTIES:
        raise ValueError(
            f"Invalid difficulty level: {difficulty}"
        )

    return True

def validate_question_count(question_count):
    """
    Validate the selected number of questions.
    """

    if question_count not in config.QUESTION_COUNTS:
        raise ValueError(
            f"Invalid question count: {question_count}"
        )

    return True