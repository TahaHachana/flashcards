## PAM and pam_faillock

What is PAM, why is it needed, and what does the pam_faillock module do?

---

**PAM (Pluggable Authentication Modules)**:
- Supplements standard Linux authentication (/etc/passwd and /etc/shadow)
- Provides flexible, customizable authentication
- Different organizations need different security levels (banks vs. small businesses)
- Allows modular approach to authentication

**pam_faillock Module** (current/recommended):
- Tracks login attempts (successes and failures)
- Blocks authentication after too many failed attempts
- Example: Lock account after 3 failed login attempts
- Prevents brute-force password attacks
- Configurable lockout duration

**Deprecated**: pam_tally2 (older version, only use if pam_faillock unavailable)

**faillock Command**: Administrators use to display login attempt information and reset locked accounts: `faillock --user username --reset`

