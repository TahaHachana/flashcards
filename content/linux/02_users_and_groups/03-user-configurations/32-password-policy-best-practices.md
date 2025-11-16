## Password Policy Best Practices

What are the best practices for implementing balanced and effective password policies in Linux environments?

---

**Balancing Security and Usability:**

**Key Principle:** Overly restrictive policies lead to workarounds (written passwords, password patterns, user frustration).

**Recommended Password Aging Settings:**

**Standard Corporate Environment:**
```bash
PASS_MAX_DAYS   90        # Quarterly changes
PASS_MIN_DAYS   1         # Prevent immediate cycling
PASS_WARN_AGE   7         # One week notice
PASS_MIN_LEN    12        # Modern standard
```

**High Security Environment:**
```bash
PASS_MAX_DAYS   60        # Bi-monthly changes
PASS_MIN_DAYS   7         # Longer wait between changes
PASS_WARN_AGE   14        # Two week notice
PASS_MIN_LEN    16        # Strong passwords
```

**Development/Testing:**
```bash
PASS_MAX_DAYS   365       # Annual changes
PASS_MIN_DAYS   0         # Can change anytime
PASS_WARN_AGE   7         # Standard warning
PASS_MIN_LEN    8         # Basic requirement
```

**Best Practice Guidelines:**

**1. Adequate Warning Period**
```bash
PASS_WARN_AGE   7
```
- Give users enough time to prepare
- Reduces expired password lockouts
- Better user experience

**2. Prevent Password Cycling**
```bash
PASS_MIN_DAYS   1
```
- At least 1 day between changes
- Defeats rapid password rotation
- Works with password history

**3. Regular but Not Excessive Rotation**
```bash
PASS_MAX_DAYS   90
```
- Balance security vs. usability
- Too frequent (30 days) → users write them down
- Too rare (365 days) → compromises go undetected

**4. Appropriate Minimum Length**
```bash
PASS_MIN_LEN    12
```
- 12+ characters recommended
- 8 characters is outdated
- Length more important than complexity

**Implementation Strategy:**

**Step 1: Document Policy**
```
Company Password Policy:
- Passwords expire every 90 days
- Minimum 12 characters
- Cannot change password more than once per day
- 7-day warning before expiration
- Cannot reuse last 5 passwords
```

**Step 2: Configure System Defaults**
```bash
# Edit /etc/login.defs
sudo vim /etc/login.defs

PASS_MAX_DAYS   90
PASS_MIN_DAYS   1
PASS_WARN_AGE   7
PASS_MIN_LEN    12
```

**Step 3: Apply to Existing Users**
```bash
# Script to update all users
for user in $(awk -F: '$3 >= 1000 {print $1}' /etc/passwd); do
    sudo chage -m 1 -M 90 -W 7 $user
done
```

**Step 4: Enforce Password Complexity (PAM)**
```bash
# /etc/security/pwquality.conf
minlen = 12
dcredit = -1    # At least 1 digit
ucredit = -1    # At least 1 uppercase
lcredit = -1    # At least 1 lowercase
ocredit = -1    # At least 1 special character
```

**Step 5: Enable Password History**
```bash
# /etc/pam.d/common-password (Debian/Ubuntu)
password required pam_pwhistory.so remember=5

# Prevents reusing last 5 passwords
```

**Special Cases and Exceptions:**

**1. Service Accounts**
```bash
# No expiration for service accounts
sudo chage -M 99999 service_account
sudo chage -E -1 service_account
```

**2. Temporary Accounts**
```bash
# Set expiration date
sudo chage -E 2025-12-31 contractor
sudo chage -M 60 contractor
```

**3. Executive Exceptions**
```bash
# Different policy for executives (if justified)
sudo chage -M 180 executive_user
# Document the exception!
```

**Regular Maintenance Tasks:**

**Weekly: Expiration Audit**
```bash
# Find accounts expiring in next 30 days
for user in $(cut -d: -f1 /etc/passwd); do
    expiry=$(sudo chage -l $user 2>/dev/null | grep "Password expires")
    # Check and report
done
```

**Monthly: Policy Compliance Check**
```bash
# Verify all users meet policy
for user in $(awk -F: '$3 >= 1000 {print $1}' /etc/passwd); do
    max_days=$(sudo chage -l $user | grep "Maximum" | awk '{print $NF}')
    if [[ $max_days -gt 90 ]]; then
        echo "$user exceeds max password age"
    fi
done
```

**User Education:**

**Password Best Practices:**
```
Good Passwords:
✓ Passphrase: "Coffee-Morning-2025-Sunrise"
✓ Random: "xK9$mP2#vL4@"
✓ Long: "ILoveMyCat2025AndCodingToo!"

Bad Passwords:
✗ Dictionary words: "password"
✗ Personal info: "maria1990"
✗ Patterns: "Password1", "Password2"
✗ Short: "Pass123"
```

**Common Pitfalls to Avoid:**

**Too Restrictive:**
- 30-day expiration → users write passwords down
- Excessive complexity → predictable patterns

**Inconsistent Enforcement:**
- Some users exempt → others feel unfair
- No monitoring → policies ignored

**Modern Recommendations (NIST):**
- Length > Complexity
- No forced periodic changes (unless compromise suspected)
- Screen against breach databases
- Allow long passphrases
- MFA on all accounts

