## Basic sudo Usage

How do you use sudo to execute a command with root privileges, and what happens when you run it?

---

**Syntax:** `sudo <command>`

**Example:** `sudo systemctl restart apache2`

**What happens:**
1. User types `sudo` before the command
2. System prompts for user's own password (not root password)
3. System checks `/etc/sudoers` to verify permission
4. Warning message displayed ("be careful on the system")
5. Command executes with root privileges
6. Returns to standard user privileges immediately after

**Note:** Password typically cached for 15 minutes after first use

