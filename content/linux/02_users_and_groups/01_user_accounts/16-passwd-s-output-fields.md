## passwd -S Output Fields

What do the fields in "passwd -S username" output mean? Interpret this example: "kgarcia P 10/29/2025 7 90 14 -1"

---

**Format**: username status lastchange min max warn inactive

**Example Interpretation**: `kgarcia P 10/29/2025 7 90 14 -1`

- **kgarcia**: Username
- **P**: Password status (P=set, L=locked, NP=no password)
- **10/29/2025**: Last password change date
- **7**: Minimum days between password changes
- **90**: Maximum days before password must change
- **14**: Warning period (days before expiration to warn user)
- **-1**: Inactivity period (-1=disabled, or days after expiration before account disabled)

**Calculation**: Password must be changed by January 27, 2026 (90 days from 10/29). User warned starting January 13, 2026 (14 days before).

**Status Codes**: P (password), L (locked), PS (password expired), NP (no password)

