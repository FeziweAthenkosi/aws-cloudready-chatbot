"""
==========================================================
AWS CloudReady Chatbot Configuration
==========================================================

This file acts as the Single Source of Truth (SSOT)
for the AWS CloudReady Chatbot.

It contains:

• Chatbot information
• Quiz types
• Difficulty levels
• Difficulty definitions
• Question count options
• AWS Categories
• AWS Services

Author: Feziwe
==========================================================

# ==========================================================
# CHATBOT INFORMATION
# ==========================================================
"""

CHATBOT_NAME = "AWS CloudReady"

CERTIFICATION = "AWS Certified Cloud Practitioner"

VERSION = "1.0"


# ==========================================================
# QUIZ TYPES
# ==========================================================

QUIZ_TYPES = [
    "Service Quiz",
    "Category Quiz",
    "Mock Exam"
]


# ==========================================================
# DIFFICULTY LEVELS
# ==========================================================

DIFFICULTIES = [
    "Easy",
    "Intermediate",
    "Difficult"
]


# ==========================================================
# DIFFICULTY DEFINITIONS
# Used by Groq when generating questions.
# ==========================================================

DIFFICULTY_DEFINITIONS = {

    "Easy": """
Generate beginner-friendly AWS Cloud Practitioner questions.

Requirements:
- Test basic AWS knowledge.
- Focus on identifying AWS services.
- Avoid long business scenarios.
- One concept per question.
- Suitable for someone starting AWS.
""",

    "Intermediate": """
Generate AWS Cloud Practitioner questions requiring moderate reasoning.

Requirements:
- Include short business scenarios.
- Compare similar AWS services.
- Require understanding of when to use each service.
- Test practical AWS knowledge.
""",

    "Difficult": """
Generate challenging AWS Cloud Practitioner questions.

Requirements:
- Include realistic business scenarios.
- Focus on architecture decisions.
- Test cost optimization.
- Test security best practices.
- Test reliability and scalability.
- Similar difficulty to the harder AWS exam questions.
"""
}


# ==========================================================
# NUMBER OF QUESTIONS
# ==========================================================

QUESTION_COUNTS = [
    1,
    5,
    10,
    20
]


# ==========================================================
# AWS CATEGORIES
# ==========================================================

AWS_CATEGORIES = {

    "Compute": [
        "Amazon EC2",
        "AWS Lambda",
        "Amazon ECS",
        "Amazon EKS",
        "AWS Fargate",
        "AWS Elastic Beanstalk",
        "Amazon Lightsail"
    ],

    "Storage": [
        "Amazon S3",
        "Amazon EBS",
        "Amazon EFS",
        "Amazon S3 Glacier",
        "AWS Backup",
        "AWS Storage Gateway"
    ],

    "Database": [
        "Amazon RDS",
        "Amazon DynamoDB",
        "Amazon Aurora",
        "Amazon Redshift",
        "Amazon ElastiCache"
    ],

    "Networking & Content Delivery": [
        "Amazon VPC",
        "Amazon Route 53",
        "Amazon CloudFront",
        "Elastic Load Balancing",
        "AWS Direct Connect",
        "AWS Transit Gateway",
        "Amazon API Gateway"
    ],

    "Security, Identity & Compliance": [
        "AWS IAM",
        "Amazon Cognito",
        "AWS KMS",
        "AWS Secrets Manager",
        "AWS Shield",
        "AWS WAF",
        "Amazon GuardDuty",
        "Amazon Inspector",
        "AWS Artifact"
    ],

    "Management & Governance": [
        "Amazon CloudWatch",
        "AWS CloudTrail",
        "AWS Config",
        "AWS Trusted Advisor",
        "AWS Organizations",
        "AWS Systems Manager",
        "AWS Control Tower",
        "AWS CloudFormation",
        "AWS Health Dashboard"
    ],

    "Migration & Transfer": [
        "AWS Application Migration Service",
        "AWS Database Migration Service",
        "AWS DataSync",
        "AWS Transfer Family",
        "AWS Snow Family"
    ],

    "Analytics": [
        "Amazon Athena",
        "AWS Glue",
        "Amazon EMR",
        "Amazon Kinesis",
        "Amazon QuickSight"
    ],

    "Machine Learning": [
        "Amazon SageMaker",
        "Amazon Bedrock",
        "Amazon Rekognition",
        "Amazon Comprehend",
        "Amazon Textract",
        "Amazon Transcribe",
        "Amazon Polly"
    ],

    "Developer Tools": [
        "AWS CodeCommit",
        "AWS CodeBuild",
        "AWS CodeDeploy",
        "AWS CodePipeline",
        "AWS Cloud9",
        "AWS X-Ray"
    ]

}


# ==========================================================
# DEFAULT VALUES
# ==========================================================

DEFAULT_QUIZ_TYPE = "Service Quiz"

DEFAULT_DIFFICULTY = "Easy"

DEFAULT_QUESTION_COUNT = 5

DEFAULT_CATEGORY = "Compute"

DEFAULT_SERVICE = "Amazon EC2"

