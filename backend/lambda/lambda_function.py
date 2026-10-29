import json
import os


def lambda_handler(event, context):
    """Simple AWS Lambda entry point for the ecommerce analytics assistant."""
    request_source = event.get("source", "unknown") if isinstance(event, dict) else "unknown"

    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "message": "Ecommerce analytics agent is online.",
                "source": request_source,
                "environment": os.getenv("AWS_REGION", "us-east-1"),
                "metrics": {
                    "revenue": "$245K",
                    "orders": 8420,
                    "conversionRate": "4.7%",
                    "topCategory": "Premium Apparel"
                }
            }
        )
    }

    return response
