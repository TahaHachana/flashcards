## Disable vs Delete Account

What are three methods to disable (not delete) a user account, and why would you choose to disable rather than delete an account?

---

**Three Methods to Disable Accounts**:

**1. Lock the Account**:
```bash
sudo usermod -L username
# or
sudo passwd -l username
```
Prevents login while keeping account intact

**2. Set Past Expiration Date**:
```bash
sudo usermod -e 1970-01-01 username
```
Account treated as expired (cannot login)

**3. Change Shell to Nologin**:
```bash
sudo usermod -s /sbin/nologin username
# or
sudo usermod -s /bin/false username
```
User cannot get interactive shell

**Why Disable Instead of Delete**:

**Advantages of Disabling**:
- **Reversible** - Can re-enable if needed
- **Preserves UID** - Files remain owned by correct user
- **Data accessible** - Files still available to admins
- **Audit trail** - Account history preserved
- **Safe approach** - No permanent data loss

**Consequences of Deleting**:
- **Permanent** - Cannot be undone
- **UID changes** - Recreating gives different UID
- **File ownership issues** - Old files orphaned
- **Data loss** - Potential loss if not backed up
- **Irreversible** - No going back

**When to Use Each**:

**Disable**: 
- Temporary situations (sabbatical, suspension)
- Uncertainty about future needs
- Want to preserve data access
- Investigation in progress

**Delete**:
- Permanent departure confirmed
- Security requirement (compromised account)
- Data already archived/transferred
- Certain no future access needed

**Re-enabling Disabled Account**:
```bash
sudo usermod -U username          # Unlock
sudo usermod -e "" username       # Remove expiration
sudo usermod -s /bin/bash username # Restore shell
```

