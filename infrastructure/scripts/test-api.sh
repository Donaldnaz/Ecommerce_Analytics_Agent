#!/usr/bin/env bash
set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-1}"
FUNCTION_NAME="${LAMBDA_FUNCTION_NAME:-ecommerce-analytics-agent}"

aws lambda invoke \
  --function-name "$FUNCTION_NAME" \
  --region "$AWS_REGION" \
  --payload '{"source":"test-api"}' \
  /tmp/lambda-output.json

cat /tmp/lambda-output.json
