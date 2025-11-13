## HTTPS Authentication

How do you authenticate when cloning private repositories via HTTPS?

---

Use Personal Access Token (not password):

1. Generate token: GitHub Settings → Developer settings → Personal access tokens
2. Clone repository:
   ```bash
   git clone https://github.com/user/private-repo.git
   # Username: your-username
   # Password: ghp_yourPersonalAccessToken
   ```

Cache credentials:
```bash
git config --global credential.helper cache
```

Modern platforms require tokens, not passwords, for HTTPS authentication.

