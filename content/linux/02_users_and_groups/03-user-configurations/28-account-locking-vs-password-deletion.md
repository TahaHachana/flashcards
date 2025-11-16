## Account Locking vs Password Deletion

What is the difference between locking an account with `passwd -l` and deleting a password with `passwd -d`, and when should each be used?

---

**Two Different Operations:**

**1. Locking an Account: `passwd -l`**

**Command:**
```bash
sudo passwd -l username
```

**What It Does:**
- Temporarily disables the account
- Adds `!` or `!!` prefix to password hash in `/etc/shadow`
- Password remains intact but is unusable
- **Can be reversed** with `passwd -u`

**How It Works:**
```bash
# Before locking:
username:$6$randomhash...:18900:0:99999:7:::

# After locking:
username:!$6$randomhash...:18900:0:99999:7:::
```

**Effect:**
- User cannot log in with password
- Password authentication disabled
- Account is suspended
- Original password preserved underneath

**Use Cases:**
- Temporary account suspension (employee on leave)
- Investigation of security issues
- Preventing access during maintenance
- Reversible account restrictions

**Unlocking:**
```bash
sudo passwd -u username
# Removes the ! prefix
# User can log in with original password
```

**2. Deleting a Password: `passwd -d`**

**Command:**
```bash
sudo passwd -d username
```

**What It Does:**
- **Permanently removes** the password from `/etc/shadow`
- Account becomes disabled
- Password cannot be recovered
- **Destructive operation** - cannot be reversed

**How It Works:**
```bash
# Before deleting:
username:$6$randomhash...:18900:0:99999:7:::

# After deleting:
username::18900:0:99999:7:::
# (password field is empty)
```

**Effect:**
- User cannot log in (no password exists)
- Account effectively disabled
- More severe than locking
- Original password is gone forever

**Use Cases:**
- Permanently disabling accounts
- Security incidents requiring complete access removal
- Accounts being decommissioned
- Before account deletion

**Comparison Table:**

| Aspect | passwd -l (Lock) | passwd -d (Delete) |
|--------|------------------|---------------------|
| **Reversible** | Yes (passwd -u) | No |
| **Password Preserved** | Yes (with ! prefix) | No (destroyed) |
| **Severity** | Temporary suspension | Permanent removal |
| **Recovery** | Simple unlock | Must set new password |
| **Use Case** | Temporary suspension | Permanent deactivation |

**Practical Scenarios:**

**Scenario 1: Employee Leave of Absence**
```bash
# Lock account (reversible)
sudo passwd -l employee

# Employee returns - unlock
sudo passwd -u employee
# Employee uses same password as before
```

**Scenario 2: Employee Terminated**
```bash
# Delete password (permanent)
sudo passwd -d former_employee

# Also expire account
sudo chage -E 0 former_employee

# Later, if account needed again:
sudo passwd former_employee
# Must set entirely new password
```

**Scenario 3: Security Incident**
```bash
# Quick response - lock immediately
sudo passwd -l compromised_user

# After investigation, if account is clean:
sudo passwd -u compromised_user

# If compromised, force new password:
sudo passwd -d compromised_user
sudo passwd compromised_user
```

**Important Notes:**

**Unlocking After Deletion Fails:**
```bash
sudo passwd -d username
sudo passwd -u username
# Error: unlocking the password would result in a passwordless account
```

Must set a new password:
```bash
sudo passwd username
```

**Best Practice:**
- Use `-l` for temporary situations (reversible)
- Use `-d` for permanent situations (destructive)
- Always consider whether you need to preserve the password
- Document which method you use and why

