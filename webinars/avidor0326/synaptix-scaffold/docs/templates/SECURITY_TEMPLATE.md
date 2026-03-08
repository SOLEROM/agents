# {{PROJECT_NAME}} — Security

> **Security Documentation**  
> Owner: CTO  
> Classification: {{INTERNAL/CONFIDENTIAL}}

---

## Security Overview

{{SECURITY_OVERVIEW}}

---

## Authentication

| Method | Usage | Location |
|--------|-------|----------|
| {{AUTH_METHOD}} | {{USAGE}} | {{ENDPOINT}} |

---

## Authorization

### Roles

| Role | Permissions |
|------|-------------|
| {{ROLE_1}} | {{PERMISSIONS}} |
| {{ROLE_2}} | {{PERMISSIONS}} |

### Access Control Model

```
{{RBAC / ABAC / Custom}}
```

---

## Data Protection

### Data Classification

| Classification | Description | Handling |
|----------------|-------------|----------|
| Public | Non-sensitive | Standard |
| Internal | Business data | Encrypted at rest |
| Confidential | PII, secrets | Encrypted + audit |

### Encryption

| Data State | Method |
|------------|--------|
| At rest | {{ENCRYPTION_METHOD}} |
| In transit | TLS 1.3 |

---

## Secrets Management

| Secret Type | Storage | Rotation |
|-------------|---------|----------|
| API keys | {{VAULT/ENV}} | {{FREQUENCY}} |
| DB credentials | {{VAULT/ENV}} | {{FREQUENCY}} |

**Never commit secrets to git.**

---

## Security Checklist

- [ ] Input validation on all endpoints
- [ ] Output encoding (XSS prevention)
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection enabled
- [ ] Rate limiting configured
- [ ] Security headers set (CSP, HSTS, etc.)
- [ ] Dependencies scanned for vulnerabilities
- [ ] Secrets not in code/logs
- [ ] Audit logging enabled

---

## Incident Response

1. **Detect:** {{DETECTION_METHOD}}
2. **Contain:** {{CONTAINMENT_STEPS}}
3. **Notify:** {{NOTIFICATION_PROCESS}}
4. **Recover:** {{RECOVERY_STEPS}}
5. **Review:** Post-incident analysis

---

## Compliance

| Standard | Status |
|----------|--------|
| {{STANDARD_1}} | {{COMPLIANT/WIP/NA}} |

---

*Last updated: {{DATE}}*
