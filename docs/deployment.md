# Deployment Guide

## Prerequisites

- AWS CLI installed and configured
- Python 3.11+
- Node.js 18+
- Access to the target AWS account and deployment role

## Infrastructure deployment

```bash
cd infrastructure/scripts
chmod +x deploy-lambda.sh
./deploy-lambda.sh
```

## Environment setup

```bash
cp .env.example .env
```

Update the variables for your AWS account and model deployment.

## Validation

```bash
cd infrastructure/scripts
./test-api.sh
```

This script sends a sample request to the deployed API to confirm the service is reachable.
