## Unlock Account Methods

A user account shows status 'L' when you run "passwd -S username". What are the two methods to unlock it, and what if it's locked due to failed login attempts?

---

**Standard Unlock Methods** (both do the same thing):

**Method 1**: `sudo passwd -u username`
**Method 2**: `sudo usermod -U username`

Both commands:
- Remove the lock from account
- Allow user to authenticate with existing password
- Do NOT change the password

**If Locked by PAM (Failed Attempts)**:

**Check failed attempts**:
`sudo faillock --user username`

**Reset failed attempt counter**:
`sudo faillock --user username --reset`

**May need both**:
1. Reset faillock counter (PAM unlock)
2. Then use passwd -u or usermod -U (system unlock)

**Verification**:
- `sudo passwd -S username` should show 'P' not 'L'
- `sudo getent shadow username` should show normal password field (no ! prefix)

**Before Unlocking**: Verify user identity and investigate why account was locked (security consideration).

