## deluser Enhanced Features

What three special options does the deluser command (Debian) provide that userdel doesn't, and when would you use each?

---

**deluser** (Debian-based systems) provides enhanced features beyond standard userdel:

**1. --remove-all-files**
```bash
deluser --remove-all-files username
```
- Deletes ALL files owned by user system-wide
- Not just home directory - searches entire filesystem
- More comprehensive than userdel -r
- **Use with extreme caution** - can affect system files

**2. --backup-to /path/for/backup**
```bash
deluser --backup-to /backups/users username
```
- Creates backup archive before deletion
- Format: .tar.gz (compressed archive)
- Preserves data for potential future recovery
- **Best practice for important accounts**

**3. --remove-home**
```bash
deluser --remove-home username
```
- Deletes user's home directory
- Similar to userdel -r
- Does not affect files outside home directory

**Practical Example - Safe Deletion**:
```bash
sudo deluser --backup-to /backup/archived_users --remove-home contractor1
```
Creates backup archive, then removes account and home directory.

**Advantage**: More flexibility and safety features compared to basic userdel command.

