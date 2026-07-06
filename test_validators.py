from validators import (
    validate_quiz_type,
    validate_category,
    validate_service,
    validate_difficulty,
    validate_question_count
)

validate_quiz_type("Service Quiz")
validate_category("Compute")
validate_service("Compute", "Amazon EC2")
validate_difficulty("Easy")
validate_question_count(65)

print("✅ All validators passed!")