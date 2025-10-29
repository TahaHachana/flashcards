## Effective UID (EUID)

What is an Effective UID (EUID) and when is it used in Linux?

---

**Effective UID (EUID)**: Alternative UID value used in special circumstances, different from the account's actual UID.

**When Used**:

1. **Privilege Escalation**:
   - Temporarily elevating permissions
   - Running with higher privileges than normal
   - Example: sudo command changes EUID to 0 (root) while keeping real UID as original user

2. **Running Programs as Another User**:
   - Execute programs with different user's permissions
   - Needed for certain system operations
   - Example: su command changes EUID to target user

3. **Executing Scripts with Different Permissions**:
   - Run scripts as different user
   - Access resources as another identity
   - Temporary permission changes without modifying actual account

**Key Point**: Allows temporary permission changes without changing the actual account UID.

**Difference from Regular UID**:
- Real UID: Actual account identifier
- Effective UID: Permissions currently in effect
- System checks EUID for access control decisions
- Used for setuid programs and permission management

