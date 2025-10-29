## Why Account Deletion is Irreversible

Why can't deleted user accounts be truly "recovered" even if you recreate them with the same username? What's the alternative to deletion?

---

**The UID Problem**:
- Deleted account had UID 1001
- Recreate same username gets NEW UID 1002
- Different UID = different identity to Linux
- Old files still owned by UID 1001
- New account (UID 1002) doesn't own those files
- Permissions won't work as expected
- NO "undo" function exists

**Example**:
```
Original: kgarcia (UID 1001)
Delete account
Recreate: kgarcia (UID 1002) ← Different UID!
Files owned by 1001 ≠ Files owned by 1002
```

**Better Alternative - DISABLE Instead of Delete**:

**Disable Methods**:
- Lock account: `usermod -L username`
- Set past expiration: `usermod -e 1970-01-01 username`
- Change to nologin: `usermod -s /sbin/nologin username`

**Benefits**: Reversible, preserves UID, files remain accessible, can re-enable if needed.

**When to Delete vs Disable**: Disable for temporary/uncertain situations; delete only for permanent departures with no data needs.

