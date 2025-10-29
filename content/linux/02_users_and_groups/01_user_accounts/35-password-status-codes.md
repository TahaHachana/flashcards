## Password Status Codes

In the output of "passwd -S username", what do the status codes L, P, PS, and NP indicate? Which ones prevent login?

---

**Password Status Codes** (second field in passwd -S output):

**P - Password Set**:
- Valid password exists
- Account can authenticate normally
- User can log in
- **Login: ALLOWED**

**L - Locked**:
- Account is locked (administratively disabled)
- Valid password may exist but cannot be used
- Account cannot authenticate
- **Login: DENIED**

**PS - Password Set but Expired**:
- Password exists but has expired
- User can log in once to change password
- Must change password before proceeding
- **Login: ALLOWED (but forced password change)**

**NP - No Password**:
- No password has been set
- Most systems won't allow login without password
- Account effectively unusable
- **Login: DENIED (on most systems)**

**Example Outputs**:
```bash
kgarcia P 10/29/2025 7 90 14 -1    ← Can login normally
jsmith L 10/15/2025 0 99999 7 -1   ← Cannot login (locked)
alee PS 08/01/2025 7 90 14 30      ← Can login but must change password
newuser NP 10/29/2025 0 99999 7 -1 ← Cannot login (no password)
```

**Fix Methods**:
- L → Unlock: `passwd -u username`
- NP → Set password: `passwd username`
- PS → Reset password: `passwd username`

