## passwd Command Basics

How does the passwd command work differently for regular users vs. administrators? What security feature affects password entry?

---

**Regular User**: `passwd`
- Changes own password only
- Must provide current password first
- Then enter new password twice

**Administrator**: `sudo passwd username`
- Can change any user's password
- Does NOT need current password
- Can unlock locked accounts
- More powerful, requires root/sudo

**Security Feature - No Display**:
- Linux does NOT display characters when typing passwords
- No asterisks, dots, or any visual feedback
- Screen appears unresponsive
- Prevents observers from counting password length
- Long-standing Unix security tradition

**Why No Display**: Additional security layer - even shoulder surfers can't determine password length or complexity.

