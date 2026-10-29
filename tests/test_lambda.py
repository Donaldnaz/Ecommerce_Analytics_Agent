import json

from backend.lambda.lambda_function import lambda_handler


def test_lambda_handler_returns_success():
    response = lambda_handler({"source": "unit-test"}, None)

    assert response["statusCode"] == 200
    payload = json.loads(response["body"])
    assert payload["message"] == "Ecommerce analytics agent is online."
    assert payload["metrics"]["topCategory"] == "Premium Apparel"
