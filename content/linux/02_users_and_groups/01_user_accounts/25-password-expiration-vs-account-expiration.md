## Password Expiration vs Account Expiration

What's the difference between password expiration and account expiration? How does each affect login, and which commands check each?

---

**Password Expiration**:
- Password needs changing
- Account still usable after password change
- User can log in once, forced to change password immediately
- Set with: `passwd -x days username`
- Check with: `chage -l username` (look at "Password expires")

**Account Expiration**:
- Entire account disabled
- Cannot log in at all, even with correct password
- Useful for temporary employees/contractors
- Set with: `usermod -e YYYY-MM-DD username` or `chage -E YYYY-MM-DD username`
- Check with: `chage -l username` (look at "Account expires")

**Key Difference**:
- Password expired = Can log in to change password
- Account expired = Cannot log in at all

**Unlock Methods**:
- Password: `passwd username` (sets new password)
- Account: `chage -E -1 username` (never expires) or set new date

**User Experience**: Password expiration prompts for new password; account expiration shows "account expired" error.

