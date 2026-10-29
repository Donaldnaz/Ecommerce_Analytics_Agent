# Security Notes

## Recommended Controls

- Enforce MFA for all AWS administrative access
- Use AWS Secrets Manager or SSM Parameter Store for secrets
- Apply least-privilege IAM policies
- Enable AWS CloudTrail and GuardDuty for operational monitoring
- Limit API exposure with authentication and authorization layers

## Application Hardening

- Validate and sanitize all request payloads
- Restrict model context to approved business data
- Log access patterns without exposing sensitive customer-level details
- Maintain dependency updates for frontend and backend packages
