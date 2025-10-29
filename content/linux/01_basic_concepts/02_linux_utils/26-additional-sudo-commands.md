## Additional sudo Commands

What are some useful sudo command variations beyond the basic `sudo <command>`?

---

- `sudo -i` - Start interactive root shell (similar to su -)
- `sudo -s` - Start shell as root with current environment
- `sudo -l` - List allowed sudo commands for current user
- `sudo -u username command` - Execute command as specified user (not root)
- `sudo visudo` - Safely edit the /etc/sudoers file

These variations provide flexibility for different administrative scenarios.

