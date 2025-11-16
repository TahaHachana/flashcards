## Password Aging Security Concepts

Explain the security rationale behind PASS_MIN_DAYS and how it prevents users from circumventing password policies.

---

**PASS_MIN_DAYS Purpose:**
Defines the minimum number of days that must pass before a user can change their password again.

**Configuration:**
```bash
PASS_MIN_DAYS   1       # Must wait 1 day
```

**The Security Problem It Solves:**

**Without PASS_MIN_DAYS (set to 0):**

Many organizations maintain password history (remember last 5-10 passwords) to prevent password reuse. However, without PASS_MIN_DAYS, users can defeat this:

```
Day 1, 9:00 AM: Forced to change password from "Winter2024!"
Day 1, 9:01 AM: Change to "Temp1234"
Day 1, 9:02 AM: Change to "Temp2345"
Day 1, 9:03 AM: Change to "Temp3456"
Day 1, 9:04 AM: Change to "Temp4567"
Day 1, 9:05 AM: Change to "Temp5678"
Day 1, 9:06 AM: Change back to "Winter2024!"
```

**Result:** User defeats password history policy by rapidly cycling through passwords in minutes.

**With PASS_MIN_DAYS (set to 1):**

```
Day 1, 9:00 AM: Change password from "Winter2024!" to "Spring2025!"
Day 1, 9:01 AM: Try to change password again
System: "You must wait longer to change your password"
Result: User must use "Spring2025!" for at least 1 day
```

**Benefits:**

**1. Enforces Password History:**
User can't quickly cycle through required number of unique passwords to return to old password.

**2. Prevents Rapid Password Changes:**
Forces users to actually USE new passwords for a minimum period.

**3. Supports Security Policies:**
Works with password history mechanisms to ensure password diversity over time.

**Common Values:**

| Value | Effect | Use Case |
|-------|--------|----------|
| 0 | Can change immediately | Not recommended (defeats password history) |
| 1 | Wait 1 day | Standard security (most common) |
| 7 | Wait 1 week | Stricter control |

**Implementation:**

**System-wide default:**
```bash
# In /etc/login.defs
PASS_MIN_DAYS   1
```

**Per-user setting:**
```bash
sudo chage -m 1 username
```

**Verification:**
```bash
sudo chage -l username
# Shows: Minimum number of days between password change: 1
```

**Real-World Scenario:**

**Company Policy:**
- Remember last 5 passwords
- PASS_MIN_DAYS = 1

**What Happens:**
1. User must change password every 90 days
2. Cannot reuse any of last 5 passwords
3. Cannot change password more than once per day
4. Takes 5 days minimum to cycle back to old password
5. By day 5, the old password is likely forgotten or less relevant

**Best Practice:**
Set PASS_MIN_DAYS to at least 1 day to prevent password policy circumvention through rapid password cycling.

