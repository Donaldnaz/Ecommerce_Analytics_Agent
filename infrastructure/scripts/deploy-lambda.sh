#!/usr/bin/env bash
set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-1}"
FUNCTION_NAME="${LAMBDA_FUNCTION_NAME:-ecommerce-analytics-agent}"
ARCHIVE_PATH="/tmp/ecommerce-analytics-agent.zip"

cd "$(dirname "$0")/../../"

zip -r "$ARCHIVE_PATH" backend/lambda

aws lambda create-function \
  --function-name "$FUNCTION_NAME" \
  --runtime python3.11 \
  --role "arn:aws:iam::${AWS_ACCOUNT_ID}:role/service-role/${FUNCTION_NAME}-role" \
  --handler lambda_function.lambda_handler \
  --zip-file "fileb://$ARCHIVE_PATH" \
  --region "$AWS_REGION" \
  --timeout 30 \
  --memory-size 512 || \
aws lambda update-function-code \
  --function-name "$FUNCTION_NAME" \
  --zip-file "fileb://$ARCHIVE_PATH" \
  --publish \
  --region "$AWS_REGION"

printf "Deployment complete for %s\n" "$FUNCTION_NAME"
