## Temporary Account Expiration

How do you set an account to automatically expire on a specific date, and what are practical use cases for this feature?

---

**Setting Account Expiration:**

**Command:**
```bash
sudo chage -E YYYY-MM-DD username
```

**Examples:**
```bash
# Expire on December 31, 2025
sudo chage -E 2025-12-31 contractor

# Expire on June 30, 2026
sudo chage -E 2026-06-30 intern

# Expire immediately (today)
sudo chage -E 0 username

# Remove expiration (never expire)
sudo chage -E -1 username
```

**What Happens When Account Expires:**

**On Expiration Date:**
- User cannot log in
- Authentication completely denied
- Account is locked
- No grace period

**Login Attempt After Expiration:**
```
login: contractor
Password: [enters password]
Your account has expired; please contact your system administrator
```

**Practical Use Cases:**

**1. Temporary Contractors**
Contractor hired for 6-month project ending June 30, 2026
```bash
sudo useradd -m contractor_smith
sudo passwd contractor_smith
sudo chage -E 2026-06-30 contractor_smith
sudo chage -M 60 contractor_smith
```
**Result:** Account automatically locks on June 30, no manual intervention needed.

**2. Intern Programs**
Summer intern program runs June 1 - August 31
```bash
sudo useradd -m intern_maria
sudo chage -E 2025-08-31 intern_maria
```

**3. Time-Limited Access (Vendors)**
External vendor needs 30-day access for project
```bash
# Calculate expiration date (30 days from now)
EXPIRY=$(date -d "+30 days" +%Y-%m-%d)
sudo chage -E $EXPIRY vendor_account
```

**4. Compliance Requirements**
Regulatory policy requires accounts to expire after 1 year of inactivity
```bash
sudo chage -E 2026-11-16 dormant_user
```

**5. Project-Based Access**
User needs access only for duration of specific project
```bash
# Project ends March 15, 2026
sudo chage -E 2026-03-15 project_user
```

**Verification and Management:**

**Check Expiration Status:**
```bash
sudo chage -l username
# Output shows:
# Account expires: Jun 30, 2026
```

**Extend Expiration:**
```bash
# Project extended by 3 months
sudo chage -E 2026-09-30 contractor
```

**Remove Expiration:**
```bash
# Convert to permanent employee
sudo chage -E -1 former_contractor
```

**Combining with Password Expiration:**

**Complete Temporary Account Setup:**
```bash
# Create contractor account
sudo useradd -m contractor_jones
sudo passwd contractor_jones

# Password policy: 60 days max, 1 day min, 7 day warning
sudo chage -m 1 -M 60 -W 7 contractor_jones

# Account expires when contract ends (Dec 31, 2025)
sudo chage -E 2025-12-31 contractor_jones

# Force initial password change
sudo passwd -e contractor_jones
```

**Difference Between Account and Password Expiration:**

**Password Expiration (PASS_MAX_DAYS or -M):**
- Password expires
- User can log in but must change password
- User can set new password themselves
- Recoverable by user

**Account Expiration (-E):**
- Entire account becomes inactive
- User cannot log in at all
- Administrator must intervene
- Not recoverable by user

**Reactivating Expired Accounts:**
```bash
# Remove expiration
sudo chage -E -1 username

# Or set new expiration date
sudo chage -E 2026-12-31 username
```

**Best Practices:**
1. Set expiration during account creation
2. Document expiration dates
3. Set up reminders to check expiring accounts
4. Notify users before expiration
5. Regular review process for accounts nearing expiration

