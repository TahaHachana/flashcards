## The sudo Command Purpose

What does sudo stand for, and how does it solve the problems associated with su?

---

**sudo** stands for "Superuser Do"

**How it solves su problems:**
- Allows execution of specific commands with root privileges
- Users authenticate with their own password (not root password)
- Granular control over which commands users can run
- Full audit trail of all sudo usage
- Easy to revoke access by editing `/etc/sudoers`
- Can delegate specific tasks to users/groups
- No need to share root password
- Better accountability (tracks who did what and when)

