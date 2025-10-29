## Minimum Password Age Purpose

Why would you set a minimum password age with "passwd -n 7 username"? What problem does this prevent?

---

**Purpose**: Prevents users from rapidly cycling back to their old password, which would defeat password expiration policies.

**The Problem Without Minimum Age**:
```
Day 1: User forced to change expired password
       Changes from "OldPassword" to "NewPassword1"
Day 1 (5 seconds later): User immediately changes back
       Changes from "NewPassword1" to "OldPassword"
Result: Password expiration defeated!
```

**With 7-Day Minimum Age**:
```
Day 1: User forced to change password
       Changes to "NewPassword1"
Day 1-7: Cannot change password again
Day 8: Can change password if desired
Result: Must use new password for at least 7 days
```

**Command**: `sudo passwd -n 7 username`

**Common Values**:
- 0 days = Can change immediately (default)
- 1 day = Once per day maximum
- 7 days = Weekly minimum (common)
- 14 days = Bi-weekly minimum

**Enforces**: Password history effectiveness by preventing immediate reversion to old passwords.

