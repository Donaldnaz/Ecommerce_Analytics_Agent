# Ecommerce Analytics Agent

An AI-powered commerce analytics assistant that helps sales teams understand customer behavior, revenue trends, and operational signals across an ecommerce storefront.

## Overview

This repository contains a lightweight full-stack prototype with:

- A React frontend for dashboard interactions
- A Python Lambda backend for serverless analytics APIs
- An agent layer for orchestration and prompt logic
- Infrastructure as code for IAM and deployment automation
- Testing scaffolding for backend validation

## Repository structure

- `frontend/` – dashboard UI
- `backend/` – serverless API logic
- `agent/` – orchestration layer
- `infrastructure/` – IAM and deployment scripts
- `docs/` – architecture and operations documentation
- `tests/` – automated tests

## Quick start

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend/lambda
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python lambda_function.py
```

### Agent

```bash
cd agent
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
python app.py
```

## Environment variables

Copy `.env.example` to `.env` and fill in your values.

## License

MIT
