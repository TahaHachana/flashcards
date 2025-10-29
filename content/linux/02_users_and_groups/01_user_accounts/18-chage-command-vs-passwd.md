## chage Command vs passwd

Compare "passwd -S" and "chage -l" for checking password information. Which is preferred for verification and why?

---

**passwd -S username**:
- Summary format: one line
- Shows: status, dates, numeric values
- Requires interpretation
- Quick check
- Example: `kgarcia P 10/29/2025 7 90 14 -1`

**chage -l username** (PREFERRED):
- Detailed format: multiple labeled lines
- Plain English descriptions
- Shows calculated expiration dates
- Easier to read and understand
- Better for documentation
- Self-explanatory output

**Example chage -l Output**:
```
Last password change                    : Oct 29, 2025
Password expires                        : Jan 27, 2026
Minimum number of days between change   : 7
Maximum number of days between change   : 90
Number of days of warning               : 14
```

**Best Practice**: Use `chage -l` for verification and documentation; use `passwd -S` for quick status checks.

