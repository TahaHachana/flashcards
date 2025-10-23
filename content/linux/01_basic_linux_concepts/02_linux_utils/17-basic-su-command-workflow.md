## Basic su Command Workflow

Describe the complete workflow for using `su -` to perform an administrative task and return to your standard user account.

---

1. Log in as standard user
2. Type `su -` (prompts for root password)
3. Enter root password
4. Verify with `whoami` - should show "root"
5. Perform necessary administrative task(s)
6. Type `exit` to leave root and return to standard user
7. Verify with `whoami` - should show original username

Key: Only stay in root account as long as necessary for the specific task.

